import logging
import os
from pathlib import Path
import sys

import pytest

from topshelfsoftware_util.json import logger as json_logger
from topshelfsoftware_logging import add_log_stream, get_logger

from conftest import get_json_files

# ----------------------------------------------------------------------------#
#                               --- Globals ---                               #
# ----------------------------------------------------------------------------#
from __setup__ import TEST_EVENTS_PATH

MODULE = "json"
MODULE_EVENTS_DIR = os.path.join(TEST_EVENTS_PATH, MODULE)

# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(f"test_{MODULE}", stream=sys.stdout)
add_log_stream(json_logger, level=logging.DEBUG, stream=sys.stdout)

# ----------------------------------------------------------------------------#
#                           --- Module Imports ---                            #
# ----------------------------------------------------------------------------#
from topshelfsoftware_util.json import (  # noqa: E402
    fmt_json,
    load_json,
)


# ----------------------------------------------------------------------------#
#                                --- TESTS ---                                #
# ----------------------------------------------------------------------------#
@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["fmt_json"])
)
def test_01_fmt_json(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    input: dict = get_event_as_dict["input"]
    expected_output: str = get_event_as_dict["expected_output"]
    fmt_str = fmt_json(input)
    assert fmt_str == expected_output


@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["load_json"])
)
def test_02_load_json(get_event_as_dict, event_dir, event_file):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    file = Path(os.path.join(event_dir, event_file))
    full_dict = load_json(file)
    assert full_dict == get_event_as_dict
