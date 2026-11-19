import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging(
    level: str = "INFO",
    log_dir: Path | None = None,
    log_file: str = "walmart_demand.log",
) -> None:
    """Configure console and rotating file logging."""

    resolved_level = getattr(logging, level.upper(), None)

    if not isinstance(resolved_level, int):
        raise ValueError(f"Invalid logging level: {level}")

    if log_dir is None:
        log_dir = Path("logs")

    log_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        log_dir / log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(resolved_level)

    root_logger.handlers.clear()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
