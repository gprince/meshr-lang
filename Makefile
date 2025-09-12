# Makefile

ANTLR_JAR = grammar/antlr-4.13.2-complete.jar
GRAMMAR_FILE = grammar/MeshrModule.g4
GEN_DIR = grammar/generated

.PHONY: all clean grammar test test-stdlib test-failures docs docs-pdf docs-html docs-clean

all: 
	$(MAKE) grammar
	$(MAKE) test
	$(MAKE) test-stdlib

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

clean: docs-clean
	rm -rf $(GEN_DIR)/*.py $(GEN_DIR)/*.tokens $(GEN_DIR)/*.interp
