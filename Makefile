SHELL = /bin/bash

.PHONY: build

build:
	. .venv/bin/activate
	poetry build --format wheel