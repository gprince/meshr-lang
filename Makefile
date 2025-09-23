# Makefile

ANTLR_JAR = grammar/antlr-4.13.2-complete.jar
GRAMMAR_FILE = grammar/MeshrModule.g4
GEN_DIR = grammar/generated
VENV_DIR = ./lsp/server/.venv
VENV_PYTHON = $(VENV_DIR)/bin/python
VENV_PIP = $(VENV_PYTHON) -m pip

.PHONY: all clean grammar test test-stdlib test-examples test-failures docs docs-pdf docs-html docs-clean lsp lsp-install lsp-test lsp-clean lsp-package lsp-install-extension ensure-venv lsp-build-server lsp-all

ensure-venv:
	@echo "🔄 Vérification de l'environnement virtuel ($(VENV_DIR))"
	@MESHR_VENV_DIR=$(VENV_DIR) bash -lc 'source tools/ensure_venv.sh'

all: 
	$(MAKE) grammar
	$(MAKE) test
	$(MAKE) test-stdlib
	$(MAKE) test-examples

grammar:
	mkdir -p $(GEN_DIR)
	touch $(GEN_DIR)/__init__.py
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor -o $(GEN_DIR) $(GRAMMAR_FILE)

test: ensure-venv
	@echo "Running parser on test files:"
	@status=0; \
	for file in $(shell find tests -name '*.meshr' ! -name 'invalid-*'); do \
		echo "Expect valid → $$file"; \
		if ! PYTHONPATH=. $(VENV_PYTHON) tests/parse_module.py $$file; then \
			echo "❌ KO: $$file"; \
			status=1; \
		fi; \
	done; \
	for file in $(shell find tests -name 'invalid-*.meshr'); do \
		echo "Expect invalid → $$file (should fail)"; \
		if PYTHONPATH=. $(VENV_PYTHON) tests/parse_module.py $$file > /dev/null 2>&1; then \
			echo "🚨 Unexpected success: $$file"; \
			status=1; \
		else \
			echo "✅ Correctly failed: $$file"; \
		fi; \
	done; \
	exit $$status

test-stdlib: ensure-venv
	@echo "Testing standard library modules:"
	@PYTHONPATH=. $(VENV_PYTHON) stdlib/test_stdlib.py

test-examples: ensure-venv
	@echo "Testing example modules:"
	@PYTHONPATH=. $(VENV_PYTHON) dev_tests/test_examples.py

test-failures:
	@echo "Identifying failed tests:"
	@$(MAKE) test 2>&1 | grep -E "(❌ KO|🚨 Unexpected success)" || echo "No test failures found"

# Documentation generation
docs: docs-pdf docs-html
	@echo "✅ Documentation generated successfully!"

docs-pdf:
	@echo "Generating PDF documentation..."
	@pandoc docs/meshr-lang.md -o docs/meshr-lang.pdf --pdf-engine=tectonic
	@echo "✅ PDF generated: docs/meshr-lang.pdf"

docs-html:
	@echo "Generating HTML documentation..."
	@pandoc docs/meshr-lang.md -o docs/meshr-lang.html --standalone --css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown-light.min.css
	@echo "✅ HTML generated: docs/meshr-lang.html"

docs-clean:
	@echo "Cleaning generated documentation..."
	@rm -f docs/meshr-lang.pdf docs/meshr-lang.html
	@echo "✅ Documentation cleaned"

# LSP Development
lsp: lsp-install
	@echo "✅ LSP setup completed"

lsp-install: ensure-venv
	@echo "Installing LSP server dependencies..."
	@$(VENV_PYTHON) -m ensurepip --upgrade
	@$(VENV_PIP) install -r lsp/server/requirements.txt
	@echo "Installing LSP client dependencies..."
	@cd lsp/client && npm install
	@echo "Compiling LSP client..."
	@cd lsp/client && npm run compile
	@echo "✅ LSP dependencies installed"

lsp-test: ensure-venv
	@echo "Testing LSP server..."
	@PYTHONPATH=. $(VENV_PYTHON) lsp/tests/test_lsp.py
	@echo "✅ LSP tests completed"

lsp-build-server: ensure-venv
	@echo "Building standalone LSP server executable..."
	@$(VENV_PYTHON) lsp/server/build_server.py
	@echo "✅ Standalone server built"

lsp-package: lsp-build-server
	@echo "Packaging LSP extension..."
	@cd lsp/client && npm run compile
	@cd lsp/client && npm run bundle
	@cd lsp/client && vsce package --allow-missing-repository --no-dependencies
	@echo "✅ LSP extension packaged"

lsp-install-extension:
	@echo "Installing LSP extension..."
	@cd lsp/client && LATEST_VSIX=$$(ls -t meshr-lang-*.vsix 2>/dev/null | head -n1) && \
		if [ -n "$$LATEST_VSIX" ]; then \
			cursor --install-extension "$$LATEST_VSIX" || echo "Impossible d'installer via Cursor"; \
		else \
			echo "❌ Aucun package VSIX trouvé"; \
		fi
	@echo "✅ LSP extension installed"

lsp-all: lsp-install lsp-package lsp-install-extension
	@echo "🚀 LSP build, package, and installation completed"

lsp-clean:
	@echo "Cleaning LSP build files..."
	@rm -rf lsp/client/out
	@rm -rf lsp/client/node_modules
	@rm -f lsp/client/*.vsix
	@echo "✅ LSP cleaned"

clean: docs-clean lsp-clean
	rm -rf $(GEN_DIR)/*.py $(GEN_DIR)/*.tokens $(GEN_DIR)/*.interp
