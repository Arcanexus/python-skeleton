import logging
import json
import pytest
from src.logger import get_logger, CustomFormatter, JsonFormatter, LogfmtFormatter


def test_custom_formatter(caplog):
    logger = get_logger(__name__, level=logging.DEBUG, format_type='console')
    with caplog.at_level(logging.DEBUG):
        logger.info("Hello, UP World!")
        logger.info("Hello, DOWN World!")
        logger.debug("This is a debug message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")

    assert "Logger initialized with the following parameters : log_level=DEBUG, log_format=console" in caplog.text
    assert "Hello, UP World!" in caplog.text
    assert "Hello, DOWN World!" in caplog.text
    assert "This is a debug message" in caplog.text
    assert "This is a warning message" in caplog.text
    assert "This is an error message" in caplog.text
    assert "This is a critical message" in caplog.text


def test_json_formatter(caplog):
    logger = get_logger(__name__, level=logging.DEBUG, format_type='json')
    with caplog.at_level(logging.DEBUG):
        logger.info("Hello, UP World!")
        logger.info("Hello, DOWN World!")
        logger.debug("This is a debug message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")

    for record in caplog.records:
        log_record = record.message
        assert log_record in [
            "Logger initialized with the following parameters : log_level=DEBUG, log_format=json",
            "Hello, UP World!",
            "Hello, DOWN World!",
            "This is a debug message",
            "This is a warning message",
            "This is an error message",
            "This is a critical message"
        ]


def test_logfmt_formatter(caplog):
    logger = get_logger(__name__, level=logging.DEBUG, format_type='logfmt')
    with caplog.at_level(logging.DEBUG):
        logger.info("Hello, UP World!")
        logger.info("Hello, DOWN World!")
        logger.debug("This is a debug message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")

    for message in caplog.messages:
        assert message in [
            "Logger initialized with the following parameters : log_level=DEBUG, log_format=logfmt",
            "Hello, UP World!",
            "Hello, DOWN World!",
            "This is a debug message",
            "This is a warning message",
            "This is an error message",
            "This is a critical message"
        ]
