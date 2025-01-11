import requests
import pytest
import allure


@allure.feature("Posts")
@allure.story("Posts")
def test_all_objects(info, starting):
    print("Start testing")
    response = requests.get('http://167.172.172.115:52353/object').json()
    assert len(response) < 10, 'Not all objects'


@allure.feature("Get posts")
@allure.story("Posts")
@pytest.mark.medium
@allure.title('Получение одного поста')
def test_one_object(new_object, info):
    with allure.step(f"Run get request for post with id {new_object}"):
        response = requests.get(
            f'http://167.172.172.115:52353/object/{new_object}'
        ).json()
    with allure.step(f'Check that post id is {new_object}'):
        assert response['id'] == new_object


@pytest.mark.parametrize(
    'name', ['Azamat', 'Farkhutdinov']
)
@pytest.mark.critical
@allure.story("Posts")
@allure.feature("Create")
@allure.title('Создание нового поста')
def test_post_object(name, info):
    with allure.step('Prepare test data'):
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
    with allure.step('Run request to create a post'):
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 201'):
        assert response.status_code == 200
    with allure.step('Check id of created post > 2000'):
        assert response.json()['id'] > 2000


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


@allure.feature("Manipulate posts")
@allure.story("Posts")
def test_put_object(new_object, info):
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


@allure.feature("Manipulate posts")
@allure.story("Posts")
def test_patch_object(new_object, starting, info):
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


@allure.feature('Equals')
@allure.story("Example")
@allure.issue(
    url='https://cdn-icons-png.flaticon.com/512/7194/7194719.png',
    name='ST-143'
)
def test_three():
    assert 1 == 1
