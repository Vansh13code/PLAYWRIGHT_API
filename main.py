import pytest
from playwright.sync_api import expect
import requests
def test_get_users():
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    data = res.json()
    assert res.status_code == 200
def test_create_post():

    payload = {
        "title": "Vansh",
        "body": "Learning API Testing",
        "userId": 1
    }

    res = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    data = res.json()


    print(res.status_code)

    print(res.headers)

    print(res.json())
    assert res.status_code == 201

    assert "application/json" in res.headers["Content-Type"]

    assert data["title"] == "Vansh"

def test_update_post():

    payload = {
        "id": 1,
        "title": "Updated Vansh",
        "body": "Updated API Testing",
        "userId": 1
    }

    res = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=payload
    )

    data = res.json()

    print(data)

    assert res.status_code == 200

    assert data["title"] == "Updated Vansh"