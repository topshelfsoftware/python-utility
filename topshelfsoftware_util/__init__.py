import logging
from typing import List, Union

from topshelfsoftware_util.aws import logger as aws_logger
from topshelfsoftware_util.common import logger as common_logger
from topshelfsoftware_util.io import logger as io_logger
from topshelfsoftware_util.platform import logger as platform_logger

PACKAGE_NAME = "topshelfsoftware-util"
LOG_LEVEL = logging.INFO


def debug():
    """Set the package Loggers to the DEBUG level."""
    LOG_LEVEL = logging.DEBUG
    _set_logger_levels(level=LOG_LEVEL)
    return


def get_package_loggers() -> List[logging.Logger]:
    """Retrieve a list of the Loggers used in the package."""
    loggers = [
        aws_logger, common_logger, io_logger, platform_logger
    ]
    return loggers


def _set_logger_levels(level: Union[int, str]):
    loggers = get_package_loggers()
    for logger in loggers:
        logger.setLevel(level)
        for handler in logger.handlers:
            handler.setLevel(level)
    return


# initialize all package logger levels
_set_logger_levels(level=LOG_LEVEL)
