SHELL=/bin/bash
FILE=local_pypi_dir.txt
LOCAL_PYPI_DIR=$(shell cat ${FILE})
PKG_NAME=trp_custom_util
PKG_VER=0.1.0

.PHONY: build

build:
	. .venv/bin/activate
	poetry build --format wheel
	cp dist/$(PKG_NAME)-$(PKG_VER)*.whl $(LOCAL_PYPI_DIR)/$(PKG_NAME)