# Specify the target to build
all: setup test

.PHONY: setup test venv

venv:
	python3 -m venv venv
	source venv/bin/activate
	export PYTHONPATH=$src

# Install dependencies
setup:
	pip3 install -r requirements.txt

# Run pytests
test:
	python3 -m pytest