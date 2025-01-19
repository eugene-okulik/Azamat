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
def test_post_object(create_post_endpoint, data):
    create_post_endpoint.create_new_post(data)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_title_correct(data['name'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(create_post_endpoint, data):
    create_post_endpoint.create_new_post(data)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_title_correct(data['name'])
    create_post_endpoint.check_bad_request()


def test_put_object(update_post_endpoint, post_new_object):
    body = {
        'name': 'Modified_object',
        'data': {
            'color': 'strawberry',
            'size': 'XL'
        }
    }
    new_id = post_new_object.new_object()
    update_post_endpoint.make_changes_in_post(new_id, body)
    update_post_endpoint.check_response_title_correct(body['name'])


def test_all_objects(get_all_objects):
    get_all_objects.get_objects()
    get_all_objects.check_count_objects()


def test_one_object(post_new_object, get_one_object):
    new_id = post_new_object.new_object()
    get_one_object.get_object(new_id)
    get_one_object.check_id_post(new_id)


def test_patch_object(patch_name_object, post_new_object):
    new_id = post_new_object.new_object()
    patch_name_object.make_changes_in_post(new_id)
    patch_name_object.check_name_patch()
