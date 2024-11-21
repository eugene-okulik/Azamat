import requests


def all_objects():
    response = requests.get('http://167.172.172.115:52353/object').json()
    print(response)
    assert len(response) < 10, 'Not all objects'


def one_object():
    post_id = new_object()
    response = requests.get(
        f'http://167.172.172.115:52353/object/{post_id}'
        ).json()
    print(response)
    assert response['id'] == post_id


def post_object():
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
    print(response.json())


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
    return response.json()['id']


def clear(object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


def put_object():
    object_id = new_object
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
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
        ).json()
    print(response)
    assert response['name'] == 'Modified_object'
    clear()


def patch_object():
    object_id = new_object
    body = {
        'name': 'New_name_object'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
        ).json()
    print(response)
    clear()


def delete_object():
    object_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response)


one_object()
all_objects()
post_object()
put_object()
patch_object()
delete_object()
