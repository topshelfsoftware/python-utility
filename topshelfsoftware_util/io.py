"""Support for processing input/output."""

from contextlib import contextmanager
import os
from pathlib import Path
import shutil
from tempfile import mkdtemp
from typing import Iterator, Union

from topshelfsoftware_logging import get_logger

logger = get_logger(__name__, stream=None)


@contextmanager
def cdtmp(
    tmpdir: Union[str, Path] = None, cleanup: bool = True
) -> Iterator[None]:
    """Context manager to work in temporary directory.

    Provisions directory, changes to it, then removes once context is complete.

    Parameters
    ----------
    tmpdir: str | Path, optional
        The path to use as the temp directory.
        Creates the specified directory if it does not exist.
        Default is None.

    cleanup: bool, optional
        Flag to remove the the temp directory or not.
        Default is `True`.

    Examples
    ----------
    >>> os.chdir('/home')
    >>> with cdtmp():
    >>>     # do stuff or
    >>>     raise Exception("There's no place like home.")
    >>> # Directory is now back to '/home' and the temp directory
    >>> # no longer exists
    """
    prev_dir = os.getcwd()

    # Create the temp directory
    if tmpdir is None:
        tmpdir = mkdtemp()
    else:
        # Convert to pathlib.Path if necessary
        tmpdir = Path(tmpdir) if isinstance(tmpdir, str) else tmpdir
        tmpdir = tmpdir.resolve()
        os.makedirs(tmpdir, exist_ok=True)
    os.environ["TMPDIR"] = str(tmpdir)
    logger.debug(f"temp directory: {tmpdir}")

    # Change the current working directory
    os.chdir(tmpdir)
    try:
        yield
    finally:
        os.chdir(prev_dir)
        if cleanup:
            shutil.rmtree(tmpdir, ignore_errors=True)
            logger.debug(f"deleted temp directory: {tmpdir}")
