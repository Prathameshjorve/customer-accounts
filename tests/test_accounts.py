"""Tests for the Customer Accounts REST API."""

import unittest

from service import app, db
from service.models import Account


class TestAccounts(unittest.TestCase):
    """Test Customer Accounts API."""

    def setUp(self):
        """Create test application and database."""
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

        self.client = app.test_client()

        with app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """Remove database objects."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        """Test service index."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_account(self):
        """Test account creation."""
        response = self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@example.com",
                "address": "123 Main Street",
                "phone_number": "9876543210"
            }
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "John Doe")

    def test_list_accounts(self):
        """Test account listing."""
        self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@example.com"
            }
        )

        response = self.client.get("/accounts")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_read_account(self):
        """Test reading an account."""
        self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@example.com"
            }
        )

        response = self.client.get("/accounts/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["id"], 1)

    def test_update_account(self):
        """Test updating an account."""
        self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@example.com"
            }
        )

        response = self.client.put(
            "/accounts/1",
            json={
                "name": "John Updated",
                "email": "john.updated@example.com"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "John Updated")

    def test_delete_account(self):
        """Test deleting an account."""
        self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@example.com"
            }
        )

        response = self.client.delete("/accounts/1")

        self.assertEqual(response.status_code, 204)

    def test_security_headers(self):
        """Test that security headers are present."""
        response = self.client.get("/")

        self.assertIn("X-Frame-Options", response.headers)

    def test_cors(self):
        """Test CORS response."""
        response = self.client.get(
            "/",
            headers={"Origin": "http://example.com"}
        )

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
