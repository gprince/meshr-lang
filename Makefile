# Makefile

ANTLR_JAR = grammar/antlr-4.13.2-complete.jar
GRAMMAR_FILE = grammar/MeshrModule.g4
GEN_DIR = grammar/generated

.PHONY: all clean grammar test

all: 
	$(MAKE) grammar
	$(MAKE) test

grammar:
	mkdir -p $(GEN_DIR)
	touch $(GEN_DIR)/__init__.py
	cd grammar && java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o ../grammar/generated MeshrModule.g4

test:
	@echo "Running parser on test files:"
	@status=0; \
	for file in $(shell find tests -name '*.meshr' ! -name 'invalid-*'); do \
		echo "Expect valid → $$file"; \
		PYTHONPATH=. python tests/parse_module.py $$file || status=1; \
	done; \
	for file in $(shell find tests -name 'invalid-*.meshr'); do \
		echo "Expect invalid → $$file (should fail)"; \
		if PYTHONPATH=. python tests/parse_module.py $$file > /dev/null 2>&1; then \
			echo "🚨 Unexpected success: $$file"; \
			status=1; \
		else \
			echo "✅ Correctly failed: $$file"; \
		fi; \
	done; \
	exit $$status

clean:
	rm -rf $(GEN_DIR)/*.py $(GEN_DIR)/*.tokens $(GEN_DIR)/*.interp
