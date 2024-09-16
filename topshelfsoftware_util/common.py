"""Helper functions for common programmatic actions."""

import shutil
import time
from typing import List, Union

from topshelfsoftware_logging import get_logger

logger = get_logger(__name__, stream=None)


def delay(sec: float):
    """Delay program execution by some number of seconds.

    Parameters
    ----------
    sec: float
        Number of seconds to delay.
    """
    logger.debug(f"delay {sec}s")
    time.sleep(sec)


def unique(values: Union[List[str], List[int]]) -> Union[List[str], List[int]]:
    """Generate a unique list of values.

    Parameters
    ----------
    values: list[str | int]
        List of values.

    Returns
    ----------
    list[str | int]
        The unique list of values.
    """
    unique_values = list(set(values))
    logger.debug(f"unique values: {unique_values}")
    return unique_values


def is_executable(name: str) -> bool:
    """Check whether a given command is on PATH and marked as executable.

    Parameters
    ----------
    name: str
        Name of command.

    Returns
    ----------
    bool
        `True` if command is executable, otherwise `False`.
    """
    return shutil.which(name) is not None
