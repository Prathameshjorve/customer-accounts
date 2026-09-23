"""
Database models for the Customer Accounts service.
"""

from datetime import datetime

from service import db


class Account(db.Model):
    """Customer account database model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    address = db.Column(db.String(250), nullable=True)
    phone_number = db.Column(db.String(30), nullable=True)
    date_joined = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def to_dict(self):
        """Convert an account to JSON-compatible dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number,
            "date_joined": self.date_joined.isoformat()
            if self.date_joined else None,
        }
