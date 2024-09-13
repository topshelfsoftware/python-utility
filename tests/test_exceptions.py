import os
import sys

import pytest

from topshelfsoftware_logging import get_logger

from conftest import get_json_files

# ----------------------------------------------------------------------------#
#                               --- Globals ---                               #
# ----------------------------------------------------------------------------#
from __setup__ import TEST_EVENTS_PATH

MODULE = "exceptions"
MODULE_EVENTS_DIR = os.path.join(TEST_EVENTS_PATH, MODULE)

# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(f"test_{MODULE}", stream=sys.stdout)

# ----------------------------------------------------------------------------#
#                           --- Module Imports ---                            #
# ----------------------------------------------------------------------------#
from topshelfsoftware_util.exceptions import ModuleError  # noqa: E402


# ----------------------------------------------------------------------------#
#                                --- TESTS ---                                #
# ----------------------------------------------------------------------------#
@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["module_error"])
)
def test_01_module_error(get_event_as_dict):
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    exc_msg_input: str = get_event_as_dict["input"]["exc_msg"]
    expected_output: str = get_event_as_dict["expected_output"]["exc_msg"]

    with pytest.raises(ModuleError):
        try:
            raise ModuleError(exc_msg_input)
        except ModuleError as e:
            assert str(e) == expected_output
            logger.error(e)
            raise e
