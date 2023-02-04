import logging

from trp_custom_util.aws import logger as aws_logger
from trp_custom_util.common import logger as common_logger
from trp_custom_util.io import logger as io_logger
from trp_custom_util.platform import logger as platform_logger

PACKAGE_NAME = "trp-custom-util"
LOG_LEVEL = logging.INFO


def debug():
    LOG_LEVEL = logging.DEBUG
    _set_logger_levels(level=LOG_LEVEL)
    return


def _set_logger_levels(level: logging._Level):
    aws_logger.setLevel(level)
    common_logger.setLevel(level)
    io_logger.setLevel(level)
    platform_logger.setLevel(level)
    return


# initialize all package logger levels
_set_logger_levels(level=LOG_LEVEL)
