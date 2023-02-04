"""Helper functions for common programmatic actions."""

import json
from typing import List, Union

from trp_custom_util.log import get_logger
logger = get_logger(__name__)


def fmt_json(input: dict) -> str:
    """Return formatted json as a string."""
    return json.dumps(input, default=str)


def unique(values: Union[List[str], List[int]]):
    """Generate a unique list of values."""
    unique_values = list(set(values))
    logger.debug(f"unique values: {unique_values}")
    return unique_values
