import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Create a post')
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )

        return self.response
