import logging
import os
import sys
import time

import pytest

from topshelfsoftware_util.common import logger as common_logger
from topshelfsoftware_logging import add_log_stream, get_logger

from conftest import get_json_files

# ----------------------------------------------------------------------------#
#                               --- Globals ---                               #
# ----------------------------------------------------------------------------#
from __setup__ import TEST_EVENTS_PATH

MODULE = "common"
MODULE_EVENTS_DIR = os.path.join(TEST_EVENTS_PATH, MODULE)

# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(f"test_{MODULE}", stream=sys.stdout)
add_log_stream(common_logger, level=logging.DEBUG, stream=sys.stdout)

# ----------------------------------------------------------------------------#
#                           --- Module Imports ---                            #
# ----------------------------------------------------------------------------#
from topshelfsoftware_util.common import (  # noqa: E402
    delay,
    unique,
    is_executable,
)


# ----------------------------------------------------------------------------#
#                                --- TESTS ---                                #
# ----------------------------------------------------------------------------#
@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["delay"])
)
def test_01_delay(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    delay_s = get_event_as_dict["input"]["delay_s"]
    start_time = time.time()
    delay(delay_s)
    end_time = time.time()
    assert (end_time - start_time) >= delay_s


@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["unique"])
)
def test_02_unique(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    values: list = get_event_as_dict["input"]["values"]
    type_str: str = get_event_as_dict["input"]["type"]
    expected: list = get_event_as_dict["expected_output"]["unique_values"]
    unique_values = unique(values)
    assert all(
        isinstance(item, eval(type_str)) for item in unique_values
    ), f"Not all elements are of type {type_str}"
    assert set(unique_values).issuperset(set(expected))


@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["is_executable"])
)
def test_03_is_executable(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    exec: str = get_event_as_dict["input"]["executable"]
    expected: bool = get_event_as_dict["expected_output"]
    assert is_executable(exec) == expected
