import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.get_objects import GetObjects
from endpoints.get_one import GetOneObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def get_all_objects():
    return GetObjects()


@pytest.fixture()
def get_one_object():
    return GetOneObject()


@pytest.fixture()
def post_new_object():
    body = {
            'name': 'For testing',
            'data': {'color': 'black', 'size': 'Large'}
        }
    new_object = CreateObject().create_new_object(body)
    id_object = new_object.json()['id']
    yield id_object
    DeleteObject().delete_object(id_object)


@pytest.fixture()
def patch_name_object():
    return PatchObject()


@pytest.fixture()
def delete_one_object():
    return DeleteObject()
