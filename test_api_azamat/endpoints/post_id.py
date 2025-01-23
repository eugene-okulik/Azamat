import requests
import allure
from endpoints.endpoint import Endpoint


class PostNew(Endpoint):

    @allure.step('Create a post')
    def new_object(self, headers=None):
        headers = headers if headers else self.headers
        body = {
            'name': 'For testing',
            'data': {'color': 'black', 'size': 'Large'}
        }
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )

        return self.response.json()['id']
