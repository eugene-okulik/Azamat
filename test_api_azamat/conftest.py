import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.get_objects import GetObjects
from endpoints.get_one import GetOneObject
from endpoints.post_id import PostNew
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
    return PostNew()


@pytest.fixture()
def patch_name_object():
    return PatchObject()


@pytest.fixture()
def delete_one_object():
    return DeleteObject()
