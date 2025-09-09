# Makefile

ANTLR_JAR = grammar/antlr-4.13.2-complete.jar
GRAMMAR_FILE = grammar/MeshrModule.g4
GEN_DIR = grammar/generated

.PHONY: all clean grammar test

all: grammar test

grammar:
	mkdir -p $(GEN_DIR)
	touch $(GEN_DIR)/__init__.py
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor -o $(GEN_DIR) $(GRAMMAR_FILE)

test:
	PYTHONPATH=. python tests/parse_module.py

clean:
	rm -rf $(GEN_DIR)/*.py $(GEN_DIR)/*.tokens $(GEN_DIR)/*.interp
