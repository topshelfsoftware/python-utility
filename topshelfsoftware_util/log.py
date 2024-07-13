"""Supports logging functionality including creation of a logger."""

import logging
import sys
from typing import TextIO, Union

import coloredlogs

DATE_FMT = "%m-%d %H:%M:%S"
DEFAULT_FMT = (
    "[%(asctime)s] [%(levelname)8s] {%(name)s:%(lineno)d} %(message)s"
)


def get_logger(
    name: str,
    level: Union[int, str] = logging.INFO,
    stream: TextIO = sys.stderr,
    propagate: bool = False,
) -> logging.Logger:
    """Configures a logger for modules by setting the log level,
    stream handler and format. Colors the terminal output.

    Parameters
    ----------
    name: str
        The name of the logger to retrieve.

    level: logging._Level, optional
        The logging level to set the logger.
        Default is `logging.INFO`.

    stream: TextIO, optional
        The stream where log messages should be written to
        (a file-like object).
        Default adds stream to stderr.

    propagate: bool, optional
        Determines if logging messages are passed to handlers
        of ancestor loggers.
        Default is `False`.

    Returns
    -------
    logging.Logger
        The configured logger obj.
    """
    logging.basicConfig()
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = propagate
    if stream is not None:
        coloredlogs.install(
            level=level,
            logger=logger,
            stream=stream,
            fmt=DEFAULT_FMT,
            datefmt=DATE_FMT,
        )
    return logger


def add_log_stream(
    logger: logging.Logger,
    level: Union[int, str] = None,
    stream: TextIO = sys.stderr,
) -> None:
    """Send logs to an IO stream.

    Parameters
    ----------
    logger: logging.Logger
        An existing logger.

    level: logging._Level, optional
        The logging level to set the logger.
        Default is None, which means use the logger's effective
        logging level.

    stream: TextIO, optional
        The stream where log messages should be written to
        (a file-like object).
        Default adds stream to stderr.
    """
    level = logger.getEffectiveLevel() if level is None else level
    coloredlogs.install(
        level=level,
        logger=logger,
        stream=stream,
        fmt=DEFAULT_FMT,
        datefmt=DATE_FMT,
    )
    return


def create_console_handler(
    fmt: str = DEFAULT_FMT, date_fmt: str = DATE_FMT
) -> logging.StreamHandler:
    """Create a formatted stream handler.

    Parameters
    ----------
    fmt: str, optional
        A specialized format string.
        `DEFAULT_FMT` is used if none is provided.

    date_fmt: str, optional
        A specialized date format.
        `DATE_FMT` is used if none is provided.

    Returns
    -------
    logging.StreamHandler
        A formatted handler streaming to stdout.
    """
    formatter = logging.Formatter(fmt=fmt, datefmt=date_fmt)
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)
    return handler


def clear_root_handlers() -> None:
    """Clear all handlers from the root logger."""
    root = logging.getLogger()
    root.handlers = []
    return
