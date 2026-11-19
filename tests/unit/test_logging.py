import logging

import pytest

from walmart_demand.logging_config import setup_logging


def test_setup_logging(tmp_path):
    setup_logging(
        level="INFO",
        log_dir=tmp_path,
        log_file="test.log",
    )

    logger = logging.getLogger("test_logger")
    logger.info("Test log message")

    log_file = tmp_path / "test.log"

    for handler in logging.getLogger().handlers:
        handler.flush()

    assert log_file.exists()
    assert "Test log message" in log_file.read_text(encoding="utf-8")


def test_invalid_logging_level(tmp_path):
    with pytest.raises(ValueError):
        setup_logging(level="INVALID", log_dir=tmp_path)
