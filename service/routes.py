"""
REST API routes for customer accounts.
"""

from flask import Blueprint, jsonify, request

from service import db
from service.models import Account

accounts_bp = Blueprint("accounts", __name__)


@accounts_bp.route("/", methods=["GET"])
def index():
    """Return service information."""
    return jsonify({
        "name": "Account REST API Service",
        "version": "1.0"
    }), 200


@accounts_bp.route("/accounts", methods=["POST"])
def create_account():
    """Create a customer account."""
    data = request.get_json() or {}

    required_fields = ["name", "email"]

    if any(field not in data for field in required_fields):
        return jsonify({
            "error": "name and email are required"
        }), 400

    account = Account(
        name=data["name"],
        email=data["email"],
        address=data.get("address"),
        phone_number=data.get("phone_number")
    )

    db.session.add(account)
    db.session.commit()

    return jsonify(account.to_dict()), 201


@accounts_bp.route("/accounts", methods=["GET"])
def list_accounts():
    """Return all customer accounts."""
    accounts = Account.query.all()
    return jsonify([account.to_dict() for account in accounts]), 200


@accounts_bp.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """Return one customer account."""
    account = db.session.get(Account, account_id)

    if account is None:
        return jsonify({"error": "Account not found"}), 404

    return jsonify(account.to_dict()), 200


@accounts_bp.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update a customer account."""
    account = db.session.get(Account, account_id)

    if account is None:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json() or {}

    account.name = data.get("name", account.name)
    account.email = data.get("email", account.email)
    account.address = data.get("address", account.address)
    account.phone_number = data.get(
        "phone_number",
        account.phone_number
    )

    db.session.commit()

    return jsonify(account.to_dict()), 200


@accounts_bp.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete a customer account."""
    account = db.session.get(Account, account_id)

    if account is None:
        return jsonify({"error": "Account not found"}), 404

    db.session.delete(account)
    db.session.commit()

    return "", 204
