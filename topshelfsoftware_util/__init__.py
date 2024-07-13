import logging
from typing import List, Union

from topshelfsoftware_util.common import logger as common_logger
from topshelfsoftware_util.io import logger as io_logger
from topshelfsoftware_util.json import logger as json_logger
from topshelfsoftware_util.platform import logger as platform_logger

PACKAGE_NAME = "topshelfsoftware-util"


def debug():
    """Set the package Loggers to the DEBUG level."""
    _set_logger_levels(level=logging.DEBUG)
    return


def get_package_loggers() -> List[logging.Logger]:
    """Retrieve a list of the Loggers used in the package."""
    loggers = [common_logger, io_logger, json_logger, platform_logger]
    return loggers


def _set_logger_levels(level: Union[int, str]):
    loggers = get_package_loggers()
    for logger in loggers:
        logger.setLevel(level)
        for handler in logger.handlers:
            handler.setLevel(level)
    return
