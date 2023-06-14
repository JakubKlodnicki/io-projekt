from eat_it.app import app

UNIMPLEMENTED = 501


def test_app_has_ping_endpoint() -> None:
    # Testuje, czy aplikacja ma punkt końcowy "/ping"
    client = app.test_client()
    response = client.get(path="/ping")
    assert response.status_code == UNIMPLEMENTED



def test_app_user_create_endpoint() -> None:
    # Testuje, czy aplikacja obsługuje punkt końcowy "/users" dla żądania POST
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 200

def test_app_user_update_endpoint() -> None:
    # Testuje, czy aplikacja obsługuje punkt końcowy "/users/<id>" dla żądania PUT
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.put(path='/users/<id>', json=payload)
    assert response.status_code == 200


def test_app_user_get_endpoint() -> None:
    # Testuje, czy aplikacja obsługuje punkt końcowy "/users/<id>" dla żądania GET
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.get(path='/users/<id>', json=payload)
    assert response.status_code == 200



def test_app_user_delete_endpoint() -> None:
    # Testuje, czy aplikacja obsługuje punkt końcowy "/users/<id>" dla żądania DELETE
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.delete(path='/users/<id>', json=payload)
    assert response.status_code == 200



def test_app_user_patch_endpoint() -> None:
    # Testuje, czy aplikacja obsługuje punkt końcowy "/users/<id>" dla żądania PATCH
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.patch(path='/users/<id>', json=payload)
    assert response.status_code == 200


def test_app_users_get_endpoint() -> None:
    # Testuje, czy aplikacja obsługuje punkt końcowy "/users/<id>" dla żądania GET
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.get(path='/users/<id>', json=payload)
    assert response.status_code == 200