.PHONY: build

build:
	source .venv/bin/activate
	poetry build --format wheel