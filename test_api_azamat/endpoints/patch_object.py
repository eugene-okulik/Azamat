from endpoints.endpoint import Endpoint
import allure
import requests


class PatchObject(Endpoint):

    @allure.step('Update a post')
    def make_changes_in_object(self, new_object, headers=None):
        headers = headers if headers else self.headers
        body = {
            'name': 'New_name_object'
        }
        self.response = requests.patch(
            f'{self.url}/{new_object}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
