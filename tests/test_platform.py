import logging
import os
import sys

import pytest

from topshelfsoftware_util.platform import logger as platform_logger
from topshelfsoftware_util.log import add_log_stream, get_logger

from conftest import get_json_files

# ----------------------------------------------------------------------------#
#                               --- Globals ---                               #
# ----------------------------------------------------------------------------#
from __setup__ import TEST_EVENTS_PATH

MODULE = "platform"
MODULE_EVENTS_DIR = os.path.join(TEST_EVENTS_PATH, MODULE)

# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(f"test_{MODULE}", stream=sys.stdout)
add_log_stream(platform_logger, level=logging.DEBUG, stream=sys.stdout)

# ----------------------------------------------------------------------------#
#                           --- Module Imports ---                            #
# ----------------------------------------------------------------------------#
from topshelfsoftware_util.platform import Platform  # noqa: E402


# ----------------------------------------------------------------------------#
#                                --- TESTS ---                                #
# ----------------------------------------------------------------------------#
@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["platform"])
)
def test_01_platform(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    if sys.platform.startswith("win"):
        logger.info("testing on Windows platform")
        assert (
            Platform.is_windows()
            and not Platform.is_mac()
            and not Platform.is_linux()
        )
    elif sys.platform.startswith("linux"):
        logger.info("testing on Linux platform")
        assert (
            not Platform.is_windows()
            and not Platform.is_mac()
            and Platform.is_linux()
        )
    elif sys.platform == "darwin":
        logger.info("testing on macOS platform")
        assert (
            not Platform.is_windows()
            and Platform.is_mac()
            and not Platform.is_linux()
        )
    else:
        logger.warning("testing on unknown platform")
