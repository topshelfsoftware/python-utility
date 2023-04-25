# python-utility

A collection of python utilities.

## Makefile

A `Makefile` is provided to standardize building and publishing the Python package. Satisfy the following prerequisites to be successful:

- Install Python 3.9 and add to PATH (executable name assumed to be `python3.9`)
- Create a file named `local_pypi_dir.txt` in the project root directory (same folder as this `README`)
  - Contents of file are a single line defining the path to a local directory to be used as a local PyPI repository

### Project Dependencies

Install project dependencies by running the following command one time

```bash
# install project deps like poetry
make install
```

### Build Instructions

Simply navigate to the same folder as this `README`, and run the following command to build and publish the utility package to a local PyPI repo.

```bash
make
```

This command activates the virtual environment with `poetry` and builds the package as a wheel.

>IMPORTANT❗
>Remember to update the `PKG_VER` variable in the `Makefile` for each new package version.

## Tagging

After incrementing the package version (and merging PR), create an associated tag of the repository. Perform the following from the command line:

```bash
git tag -a <version> <commit_hash>
```

`<version>` will take the form vX.Y.Z where X.Y.Z represents MAJOR.MINOR.PATCH in semantic versioning. Then push the tag to the remote server using:

```bash
git push origin <version>
```

## Available Modules

### `aws`

Facilitates interaction with AWS using boto3 clients.

### `common`

Helper functions for data retrieval and common programmatic actions.

### `exceptions`

Define custom exceptions.

### `io`

Support for processing input/output..

### `log`

Supports logging functionality including creation of a logger and managing handlers.

### `platform`

Provides a clean way to identify platform OS.

### `test`

A utility for standardizing unit testing.
