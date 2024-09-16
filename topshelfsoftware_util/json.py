"""Work with JSON data."""

import json
from pathlib import Path
from typing import Union

from topshelfsoftware_logging import get_logger

logger = get_logger(__name__, stream=None)


def fmt_json(input: dict) -> str:
    """Return formatted JSON as a string.

    Parameters
    ----------
    input: dict
        JSON input to format.

    Returns
    ----------
    str
        The formatted JSON.
    """
    return json.dumps(input, default=str)


def load_json(file: Union[str, Path]) -> dict:
    """Loads a JSON file into a dictionary.

    Parameters
    ----------
    file: str | Path
        Path to JSON file.

    Returns
    ----------
    dict
        JSON content as a dict.
    """
    logger.debug(f"Reading JSON file: {file}")
    with open(file, "r") as f:
        dictionary: dict = json.load(f)
        logger.debug(f"dict: {fmt_json(dictionary)}")
    return dictionary
