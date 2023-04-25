"""Helper functions for common programmatic actions."""

import json
import shutil
import time
from typing import List, Union

from topshelfsoftware_util.log import get_logger
logger = get_logger(__name__)


def fmt_json(input: dict) -> str:
    """Return formatted json as a string."""
    return json.dumps(input, default=str)


def delay(sec: float):
    """Delay program execution by some number of seconds."""
    logger.debug(f"delay {sec}s")
    time.sleep(sec)


def unique(values: Union[List[str], List[int]]):
    """Generate a unique list of values."""
    unique_values = list(set(values))
    logger.debug(f"unique values: {unique_values}")
    return unique_values


def is_tool(name: str) -> bool:
    """Check whether `name` is on PATH and marked as executable."""
    return shutil.which(name) is not None
