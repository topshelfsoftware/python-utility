"""Supports logging functionality including creation of a logger."""

import logging
import sys
from typing import Union

import coloredlogs

DATE_FMT = "%m-%d %H:%M:%S"
DEFAULT_FMT = "[%(asctime)s] [%(levelname)8s] {%(name)s:%(lineno)d} %(message)s"


def get_logger(name: str,
               level: Union[int, str] = logging.INFO,
               propagate: bool = False) -> logging.Logger:
    """Configures a logger for modules by setting the log level 
    and format. Colors the terminal output.

    Parameters
    ----------
    name : str
        The name of the logger to retrieve.

    level : logging._Level, optional
        The logging level to set the logger.
        Default is `logging.INFO`.

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
    coloredlogs.install(level=level, logger=logger, stream=sys.stdout,
                        fmt=DEFAULT_FMT, datefmt=DATE_FMT)
    return logger


def create_console_handler(fmt: str = DEFAULT_FMT,
                           date_fmt: str = DATE_FMT) -> logging.StreamHandler:
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


def add_console_handler(logger: logging.Logger,
                        handler: logging.Handler = None) -> None:
    """Add console handler to the provided logger.
    
    Parameters
    ----------
    logger: logging.Logger
        An existing logger.

    handler: logging.Handler, optional
        Handler to add to the provided logger. If none is provided,
        a StreamHandler will be created and added to the logger.
    """
    if handler is None:
        handler = create_console_handler()
    logger.addHandler(handler)
    return


def clear_root_handlers() -> None:
    """Clear all handlers from the root logger."""
    root = logging.getLogger()
    root.handlers = []
    return
