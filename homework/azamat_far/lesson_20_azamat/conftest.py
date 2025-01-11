import pytest
import requests


@pytest.fixture()
def new_object():
    body = {
        'name': 'Test_object',
        'data': {
            'color': 'blueberry',
            'size': 'XXL'
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture()
def num():
    return 1
