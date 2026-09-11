"""Standard-library logging boundary for the application."""

import logging


def configure_logging(level: str = "INFO") -> logging.Logger:
    """Configure and return the package logger without business behavior."""

    normalized_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=normalized_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    return logging.getLogger("ai_quotation_intelligence")
