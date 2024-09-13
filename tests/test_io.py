import logging
import os
from pathlib import Path
import shutil
import sys

import pytest

from topshelfsoftware_util.io import logger as io_logger
from topshelfsoftware_logging import add_log_stream, get_logger

from conftest import get_json_files, print_section_break

# ----------------------------------------------------------------------------#
#                               --- Globals ---                               #
# ----------------------------------------------------------------------------#
from __setup__ import TEST_EVENTS_PATH

MODULE = "io"
MODULE_EVENTS_DIR = os.path.join(TEST_EVENTS_PATH, MODULE)

# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(f"test_{MODULE}", stream=sys.stdout)
add_log_stream(io_logger, level=logging.DEBUG, stream=sys.stdout)

# ----------------------------------------------------------------------------#
#                           --- Module Imports ---                            #
# ----------------------------------------------------------------------------#
from topshelfsoftware_util.io import cdtmp  # noqa: E402


# ----------------------------------------------------------------------------#
#                                --- TESTS ---                                #
# ----------------------------------------------------------------------------#
@pytest.mark.happy
@pytest.mark.parametrize("event_dir", [MODULE_EVENTS_DIR])
@pytest.mark.parametrize(
    "event_file", get_json_files(MODULE_EVENTS_DIR, ["cdtmp"])
)
def test_01_cdtmp(get_event_as_dict):
    print_section_break()
    logger.info(f"Test Description: {get_event_as_dict['description']}")
    tmpdir: str = get_event_as_dict["input"]["tmpdir"]
    cleanup: bool = get_event_as_dict["input"]["cleanup"]
    expected_output: bool = get_event_as_dict["expected_output"][
        "tmpdir_exists"
    ]
    with cdtmp(tmpdir, cleanup):
        cwd = Path.cwd()
        assert cwd.exists()

    assert cwd.exists() == expected_output

    if not cleanup:
        # cleanup the tmpdir as part of this test
        logger.info("cleaning up test...")
        shutil.rmtree(tmpdir, ignore_errors=True)
        logger.info(f"deleted temp directory: {tmpdir}")
