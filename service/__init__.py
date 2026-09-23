"""
Customer Accounts service package.
"""

import os

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    database_uri = os.getenv(
        "DATABASE_URI",
        "sqlite:///accounts.db"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    CORS(app)
    Talisman(app)

    from service.routes import accounts_bp
    app.register_blueprint(accounts_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
