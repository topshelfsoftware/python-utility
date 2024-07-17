# python-utility

A collection of python utilities.

## Getting Started

### Prerequisites

1. Python 3.7 | 3.8 | 3.9 | 3.10 | 3.11 installed on system
2. `aws-sam-cli` with "sam" on system path
3. Optionally, create a file named `local_pypi_dir.txt` in the project root directory (same folder as this `README`)
    - Contents of file are a single line defining the path to a local directory to be used as a local PyPI repository.

### Set Up Environment

To create the dev environment, navigate to the project root directory and run the following

```bash
make setup [PYTHON3=python3]
```

>NOTE: This command creates a virtual environment to `./.venv` and downloads all the
packages required to debug/test the source code as well as other developer tools. Specify
a minor version of Python 3 using the `PYTHON3=python3.<minor>` arg.

If the dev environment has already been setup, then the dependencies can be updated with

```bash
make update [PYTHON3=python3]
```

### Unit Tests

Unit tests are located in the `./tests` directory and are written using `pytest`.
To run all unit tests, execute the following command from the project root directory
>NOTE: For tests to pass, authentication to the correct AWS account is required

```bash
make test
```

### Formatting and Linting

To ensure consistent style and catch potential errors, this repo formats Python code using `black` and
lints Python code using `ruff`. To format and then lint, run

```bash
make format
```

## Deployment

>NOTE: AWS deployment targets also require user be authenticated with relevant AWS account

### Package and Lambda Layer

Build the `topshelfsoftware-util` Python package as a wheel and copy it to the local PyPI repository

```bash
make package
```

Further, deploy the package as a Lambda layer with

```bash
make deploy-layer AWS_PROFILE=<aws-profile> S3_BUCKET=<s3-bucket> TAGS="CustomerId={cid} ProjectId={pid}" [AWS_REGION=us-east-1]
```

## Versioning

This package uses Semantic Versioning 2.0.0 to describe MAJOR.MINOR.PATCH releases.

IMPORTANT❗
Search the project for the existing package version and update in the following places prior to building the package and deploying the lambda layer:

- `PKG_VER` variable in the project `Makefile`
- `version` in the poetry `pyproject.toml`
- `PackageVersion` parameter in the `samconfig.toml`
- `topshelfsoftware-util` package in the `lambda_layer/deps/requirements.txt`

## Available Modules

See the list of [available modules](./docs/README.md#available-modules).
