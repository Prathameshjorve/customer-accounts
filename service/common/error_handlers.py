"""Application error handlers."""

from flask import jsonify


def register_error_handlers(app):
    """Register HTTP error handlers."""

    @app.errorhandler(404)
    def not_found(error):
        """Handle resource-not-found errors."""
        return jsonify({"error": "Resource not found"}), 404

    return app
