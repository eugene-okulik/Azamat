from endpoints.endpoint import Endpoint
import allure
import requests


class UpdatePost(Endpoint):

    @allure.step('Update a post')
    def make_changes_in_post(self, new_object, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{new_object}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
