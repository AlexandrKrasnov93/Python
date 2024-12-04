import pytest
import requests

base_url = "https://ru.yougile.com/api-v2/"


@pytest.fixture
def api_token():
    api_token = "" # необходимо подставить api ключ
    return api_token


def test_getting_project(api_token):
    header = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    rest = requests.get(base_url+'projects', headers=header)
    assert rest.status_code == 200


def test_create_project(api_token):
    header = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    body = {
        "title": "Закупки"
    }
    response = requests.post(base_url+"projects", headers=header, json=body)

    assert response.status_code == 201
    id = requests.get(base_url+"projects/" + response.json()['id'], headers=header).json()['id']
    assert id == response.json()['id']


def test_to_change_data(api_token):
    header = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    body = {
        "title": "Библиотека",
    }
    response = requests.post(base_url+"projects", headers=header, json=body)
    body = {
        "title": "Библиотека v2"
    }
    response = requests.put(base_url+"projects/" + response.json()['id'], headers=header, json=body)
    title = requests.get(base_url+"projects/" + response.json()['id'], headers=header).json()["title"]
    assert title == "Библиотека v2"


def test_negative():
    header = {
        "Content-Type": "application/json"
    }
    body = {
        "title": "Госуслуги"
    }
    response = requests.post(base_url+"projects", headers=header, json=body)
    assert response.status_code == 401
