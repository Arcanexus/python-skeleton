import pytest
from unittest import mock
from src.main import print_something, main
import logging


def test_print_something(caplog):
  loglevel = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
  format = ["json", "logfmt", "custom"]
  for fmt in format:
    for lvl in loglevel:
      with caplog.at_level(logging.DEBUG):
        print_something(lvl, lvl + " - " + fmt, fmt)
      assert lvl + " - " + fmt in caplog.text
      assert lvl in caplog.text
      assert fmt in caplog.text


# @mock.patch('src.main.print_something')
# def test_main(mock_print_something):
#   main()
#   mock_print_something.assert_called_once_with("YOLO")

def test_main(caplog):
  with caplog.at_level(logging.DEBUG):
    main()

  for record in caplog.records:
    log_record = record.message
    assert log_record in [
      "json message",
      "logfmt message",
      "custom message"
    ]
