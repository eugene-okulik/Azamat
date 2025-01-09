import requests
import allure


@allure.story("Posts")
@allure.feature("Manipulate posts")
def delete_object(new_object, info):
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{new_object}'
    )
    print(response)


@allure.feature('Print')
@allure.story("Example")
def test_num(num):
    print(num)
