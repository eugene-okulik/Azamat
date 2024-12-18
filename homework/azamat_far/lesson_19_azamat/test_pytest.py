import requests
import pytest


def test_all_objects(info, starting):
    print("Start testing")
    response = requests.get('http://167.172.172.115:52353/object').json()
    assert len(response) < 10, 'Not all objects'


@pytest.mark.medium
def test_one_object(new_object, info):
    response = requests.get(
        f'http://167.172.172.115:52353/object/{new_object}'
    ).json()
    assert response['id'] == new_object


@pytest.mark.parametrize(
    'name', ['Azamat', 'Farkhutdinov']
)
@pytest.mark.critical
def test_post_object(name, info):
    body = {
        'name': 'Azm_object',
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
    assert response.status_code == 200
    assert response.json()['id'] == 1012


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
def info():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='session')
def starting():
    print('Start testing')
    yield
    print('Testing completed')


def test_put_object(new_object, info):
    print("Start testing")
    body = {
        'name': 'Modified_object',
        'data': {
            'color': 'strawberry',
            'size': 'XL'
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_object}',
        json=body,
        headers=headers
    ).json()
    print(response)
    assert response['name'] == 'Modified_object'


def test_patch_object(new_object, info):
    print("Start testing")
    body = {
        'name': 'New_name_object'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_object}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'New_name_object'


def delete_object(new_object, info):
    response = requests.delete(f'http://167.172.172.115:52353/object/{new_object}')
    print(response)
