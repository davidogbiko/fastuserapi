"""Simple User API Tests
"""
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_post_user() -> None:
    """Verify that users can be added to the database"""
    response = client.post("/users/", json={"name": "Jack Sparrow"})
    assert response.status_code == 201


def test_get_user() -> None:
    """Verify that users are available in the database"""
    response = client.get("/users/1")
    assert response.status_code == 200


def test_get_root_path() -> None:
    """Verify that users are available in the database"""
    response = client.get("/")
    assert response.status_code == 200
