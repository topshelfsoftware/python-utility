"""Work with JSON data."""

import json

from topshelfsoftware_util.log import get_logger

logger = get_logger(__name__, stream=None)


def fmt_json(input: dict) -> str:
    """Return formatted json as a string."""
    return json.dumps(input, default=str)


def load_json_schema(file: str) -> dict:
    """Loads a JSON schema file into a dictionary."""
    logger.info(f"Reading schema file: {file}")
    with open(file, "r") as f:
        schema: dict = json.load(f)
        logger.debug(f"schema: {fmt_json(schema)}")
    return schema
