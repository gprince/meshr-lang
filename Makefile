# Makefile

ANTLR_JAR = grammar/antlr-4.13.2-complete.jar
GRAMMAR_FILE = grammar/MeshrModule.g4
GEN_DIR = grammar/generated

.PHONY: all clean grammar test test-stdlib test-examples test-failures docs docs-pdf docs-html docs-clean lsp lsp-install lsp-test lsp-clean lsp-package lsp-install-extension

all: 
	$(MAKE) grammar
	$(MAKE) test
	$(MAKE) test-stdlib
	$(MAKE) test-examples

grammar:
	mkdir -p $(GEN_DIR)
	touch $(GEN_DIR)/__init__.py
	cd grammar && java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o ../grammar/generated MeshrModule.g4

test:
	@echo "Running parser on test files:"
	@status=0; \
	for file in $(shell find tests -name '*.meshr' ! -name 'invalid-*'); do \
		echo "Expect valid → $$file"; \
		PYTHONPATH=. python3 tests/parse_module.py $$file || status=1; \
	done; \
	for file in $(shell find tests -name 'invalid-*.meshr'); do \
		echo "Expect invalid → $$file (should fail)"; \
		if PYTHONPATH=. python3 tests/parse_module.py $$file > /dev/null 2>&1; then \
			echo "🚨 Unexpected success: $$file"; \
			status=1; \
		else \
			echo "✅ Correctly failed: $$file"; \
		fi; \
	done; \
	exit $$status

test-stdlib:
	@echo "Testing standard library modules:"
	@PYTHONPATH=. python3 stdlib/test_stdlib.py

test-examples:
	@echo "Testing example modules:"
	@PYTHONPATH=. python3 test_examples.py

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

lsp-install:
	@echo "Installing LSP server dependencies..."
	@cd lsp/server && pip install -r requirements.txt
	@echo "Installing LSP client dependencies..."
	@cd lsp/client && npm install
	@echo "Compiling LSP client..."
	@cd lsp/client && npm run compile
	@echo "✅ LSP dependencies installed"

lsp-test:
	@echo "Testing LSP server..."
	@PYTHONPATH=. ~/.pyenv/versions/3.12.0/bin/python3 lsp/tests/test_lsp.py
	@echo "✅ LSP tests completed"

lsp-package:
	@echo "Packaging LSP extension..."
	@cd lsp/client && npm run compile
	@cd lsp/client && vsce package --allow-missing-repository --no-dependencies
	@echo "✅ LSP extension packaged"

lsp-install-extension:
	@echo "Installing LSP extension..."
	@cd lsp/client && cursor --install-extension meshr-lang-0.1.0.vsix || echo "Cursor CLI not found, install manually"
	@echo "✅ LSP extension installed"

lsp-clean:
	@echo "Cleaning LSP build files..."
	@rm -rf lsp/client/out
	@rm -rf lsp/client/node_modules
	@rm -f lsp/client/*.vsix
	@echo "✅ LSP cleaned"

clean: docs-clean lsp-clean
	rm -rf $(GEN_DIR)/*.py $(GEN_DIR)/*.tokens $(GEN_DIR)/*.interp
