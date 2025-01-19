import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.get_objects import GetObjects
from endpoints.get_one import GetOneObject
from endpoints.post_id import PostNew
from endpoints.patch_object import PatchObject


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


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
