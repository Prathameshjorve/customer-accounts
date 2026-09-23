"""Logging configuration utilities."""

import logging


def init_logging(app):
    """Initialize application logging."""
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    if not app.logger.handlers:
        app.logger.addHandler(handler)

    app.logger.setLevel(logging.INFO)
