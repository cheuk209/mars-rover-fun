# Specify the target to build

all: setup test

.PHONY: setup test venv

PYTHONPATH:= ./src
export PYTHONPATH

venv:
	python3 -m venv venv
	source venv/bin/activate

# Install dependencies
setup:
	pip install -r requirements.txt

# Run pytests
test:
	python3 -m pytest test/