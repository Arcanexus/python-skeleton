import logging
import yaml
from logger import get_logger
import os


def print_something(lvl, msg, format):
    logger = get_logger(__name__, level=logging.DEBUG, format_type=format)
    log_method = getattr(logger, lvl.lower(), logger.info)
    log_method(msg)


def main():
    print_something("debug", "json message", 'json')
    print_something("info", "logfmt message", 'logfmt')
    print_something("warning", "custom message", 'custom')

    # logger = get_logger(__name__, level=logging.DEBUG, format_type='custom')
    # logger.info("Hello, UP World!")
    # logger.info("Hello, DOWN World!")
    # logger.debug("This is a debug message")
    # logger.warning("This is a warning message")
    # logger.error("This is an error message")
    # logger.critical("This is a critical message")

    # print()

    # logger = get_logger(__name__, level=logging.DEBUG, format_type='json')
    # logger.info("Hello, UP World!")
    # logger.info("Hello, DOWN World!")
    # logger.debug("This is a debug message")
    # logger.warning("This is a warning message")
    # logger.error("This is an error message")
    # logger.critical("This is a critical message")

    # print()

    # logger = get_logger(__name__, level=logging.DEBUG, format_type='logfmt')
    # logger.info("Hello, UP World!")
    # logger.info("Hello, DOWN World!")
    # logger.debug("This is a debug message")
    # logger.warning("This is a warning message")
    # logger.error("This is an error message")
    # logger.critical("This is a critical message")


with open(f"{os.path.dirname(os.path.abspath(__file__))}/logger.conf.yml", 'r') as file:
    logger_config = yaml.safe_load(file)
    log_level = logger_config['config']['logs']['log_level']
    log_format = logger_config['config']['logs']['log_format']
logger = get_logger(__name__, level=log_level, format_type=log_format)
# logger.debug(f"Logger initialized with the following parameters : log_level={log_level}, log_format={log_format}")

if __name__ == "__main__":
    main()
