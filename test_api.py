import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_existing_user():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Leanne Graham"
    assert body["email"] == "Sincere@april.biz"


def test_get_missing_user():
    response = requests.get(f"{BASE_URL}/users/9999", timeout=10)
    assert response.status_code == 404
    assert response.json() == {}


def test_create_post():
    payload = {
        "title": "My first API test",
        "body": "Testing with Postman",
        "userId": 1,
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body
