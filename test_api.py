import requests

def test_users():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    data = response.json()

    print(data[0]["name"])

    assert response.status_code == 200

    assert data[0]["id"] == 1