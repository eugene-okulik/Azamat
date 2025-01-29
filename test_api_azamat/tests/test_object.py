import pytest


TEST_DATA = [
    {'name': 'Azm_object', 'data': {'color': 'blueberry', 'size': 'XXL'}},
    {'name': 'Far_object', 'data': {'color': 'red', 'size': 'medium'}}
]

NEGATIVE_DATA = [
    {'name': ['Azm_object'], 'data': {'color': 'blueberry', 'size': 'XXL'}},
    {'name': {'Far_object': ''}, 'data': {'color': 'red', 'size': 'medium'}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_title_correct(data['name'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(create_object_endpoint, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_bad_request()


def test_put_object(update_object_endpoint, post_new_object):
    body = {
        'name': 'Modified_object',
        'data': {
            'color': 'strawberry',
            'size': 'XL'
        }
    }
    update_object_endpoint.make_changes_in_object(post_new_object, body)
    update_object_endpoint.check_response_title_correct(body['name'])


def test_all_objects(get_all_objects):
    get_all_objects.get_objects()
    get_all_objects.check_count_objects()


def test_one_object(post_new_object, get_one_object):
    get_one_object.get_object(post_new_object)
    get_one_object.check_id_object(post_new_object)


def test_patch_object(patch_name_object, post_new_object):
    patch_name_object.make_changes_in_object(post_new_object)
    patch_name_object.check_name_patch()


def test_delete_object(delete_one_object, post_new_object):
    delete_one_object.delete_object(post_new_object)
    delete_one_object.check_that_status_is_200()
