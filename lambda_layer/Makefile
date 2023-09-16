# This Makefile follows the custom build example laid out in the following AWS guide:
# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-layers.html#building-applications-examples
#
# The requirements.txt file in the deps folder contains a package that only exists on GitHub (no pypi server)
# so the Makefile method is required to package the Lambda layer.

SHELL := /bin/bash
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(realpath $(dir $(MAKEFILE_PATH)))
CWD := $(notdir $(patsubst %/,%,$(dir $(MAKEFILE_PATH))))
VENV_DIR := $(MAKEFILE_DIR)/../.venv
ifndef ARTIFACTS_DIR
	ARTIFACTS_DIR := $(MAKEFILE_DIR)/artifacts
endif

# function to activate the python virtual env
activate = . $(VENV_DIR)/bin/activate && $1

# build target
build-TopshelfsoftwareUtilLayer:
	@echo "Building lambda layer with makefile: $(MAKEFILE_PATH)"
	mkdir -p "$(ARTIFACTS_DIR)/python"

	@echo "Upgrading pip"
	$(call activate,python -m pip install --upgrade pip)

	@echo "Installing python packages ** with ** dependencies"
	$(call activate,python -m pip install -r $(MAKEFILE_DIR)/deps/requirements.txt -t "$(ARTIFACTS_DIR)/python" --upgrade)