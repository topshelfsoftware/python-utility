SHELL=/bin/bash
FILE=local_pypi_dir.txt
LOCAL_PYPI_DIR=$(shell cat ${FILE})
PKG_NAME=topshelfsoftware_util
PKG_VER=0.1.0

.PHONY: build

all: build copy

build:
	. .venv/bin/activate
	poetry build --format wheel

copy:
	cp dist/$(PKG_NAME)-$(PKG_VER)*.whl $(LOCAL_PYPI_DIR)