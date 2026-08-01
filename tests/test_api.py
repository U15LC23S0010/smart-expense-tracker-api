import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app import app

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200


def test_add_expense():
    response = client.post("/expenses", json={
        "title": "Test Expense",
        "amount": 100,
        "category": "Testing",
        "date": "2026-08-01"
    })

    assert response.status_code == 201


def test_category():
    response = client.get("/expenses/category/Testing")
    assert response.status_code == 200


def test_total():
    response = client.get("/expenses/total")
    assert response.status_code == 200