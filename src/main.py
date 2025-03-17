import logging
from logger import get_logger


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


logger = get_logger(__name__, level=logging.DEBUG, format_type='custom')

if __name__ == "__main__":
    main()
