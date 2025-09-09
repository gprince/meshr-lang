.PHONY: grammar test lint

# Compile ANTLR grammar
grammar:
	java -jar ./antlr-4.13.1-complete.jar -Dlanguage=Python3 -o grammar grammar/*.g4

# Run tests
test:
	pytest tests/

# Run linter
lint:
	ruff check cli/ tests/
