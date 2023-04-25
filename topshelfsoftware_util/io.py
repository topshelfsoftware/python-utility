"""Support for processing input/output."""

from contextlib import contextmanager
import os
import shutil
from tempfile import gettempdir, mkdtemp
from typing import Iterator

from topshelfsoftware_util.log import get_logger
logger = get_logger(__name__)


@contextmanager
def cdtmp(tmpdir: str = None, sub_dirname: str = None, cleanup: bool = True) -> Iterator[None]:
    """Context manager to work in temporary directory.

    Provisions directory, changes to it, then removes once context is complete.

    >>> os.chdir('/home')
    >>> with cdtmp():
    >>>     # do stuff or
    >>>     raise Exception("There's no place like home.")
    >>> # Directory is now back to '/home' and the temporary directory no longer exists
    """
    if tmpdir is not None:
        os.environ["TMPDIR"] = tmpdir
    
    try:
        prev_dir = os.getcwd()
    except FileNotFoundError:
        prev_dir = gettempdir()
        logger.warning(f"Unable to get current working directory, using {prev_dir}")
    
    if sub_dirname is not None:
        temp_dir = os.path.join(gettempdir(), sub_dirname)
        os.makedirs(temp_dir, exist_ok=True)
    else:
        temp_dir = mkdtemp()
    logger.debug(f"temp directory: {temp_dir}")
    
    os.chdir(temp_dir)
    try:
        yield
    finally:
        os.chdir(prev_dir)
        if cleanup:
            shutil.rmtree(temp_dir, ignore_errors=True)
            logger.debug(f"deleted temp directory: {temp_dir}")
