import logging
import os
import sys

import pytest

from topshelfsoftware_util.log import get_logger

from conftest import get_json_files

# ----------------------------------------------------------------------------#
#                               --- Globals ---                               #
# ----------------------------------------------------------------------------#
from __setup__ import TEST_EVENTS_PATH

MODULE = "log"
MODULE_EVENTS_DIR = os.path.join(TEST_EVENTS_PATH, MODULE)

# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(f"test_{MODULE}", stream=sys.stdout)

# ----------------------------------------------------------------------------#
#                           --- Module Imports ---                            #
# ----------------------------------------------------------------------------#
from topshelfsoftware_util.log import (  # noqa: E402
    get_logger,
    add_log_stream,
    create_console_handler,
    clear_root_handlers,
)


# ----------------------------------------------------------------------------#
#                                --- TESTS ---                                #
# ----------------------------------------------------------------------------#
@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["get_logger"])
)
def test_01_get_logger(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    input: dict = get_event_as_dict["input"]
    input["stream"] = (
        eval(input["stream"]) if "stream" in input else sys.stderr
    )
    expected_output: dict = get_event_as_dict["expected_output"]
    unit_test_logger = get_logger(**input)
    assert isinstance(unit_test_logger, logging.Logger)
    assert unit_test_logger.name == expected_output["name"]
    assert unit_test_logger.level == expected_output["level"]
    assert unit_test_logger.handlers != []
    assert unit_test_logger.propagate == expected_output["propagate"]


@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["add_log_stream"])
)
def test_02_add_log_stream(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    input: dict = get_event_as_dict["input"]
    unit_test_logger = get_logger(input["name"], stream=None)
    assert unit_test_logger.handlers == []

    add_log_stream(unit_test_logger, stream=eval(input["stream"]))
    assert unit_test_logger.handlers != []


@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["create_console_handler"])
)
def test_03_create_console_handler(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    handler = create_console_handler()
    assert isinstance(handler, logging.Handler)


@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["clear_root_handlers"])
)
def test_03_clear_root_handlers(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    clear_root_handlers()
    assert logging.getLogger().handlers == []
