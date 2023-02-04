# python-utility

A collection of python utilities.

## Build Instructions

1. Navigate to the same folder as this README.
2. Activate python environment with `poetry`.
3. `poetry build --format wheel`

A `Makefile` is provided to build the wheel and copy it into a local PyPI directory. This requires a file in the project folder named `local_pypi_dir.txt` - the contents of which are a single line defining the path to a local directory. Remember to update the `PKG_VER` variable in the `Makefile` for each new package version.

## Tagging

After incrementing the package version, create an associated tag of the repository. Perform the following from the command line:

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
