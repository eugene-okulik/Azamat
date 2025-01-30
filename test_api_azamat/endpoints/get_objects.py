import requests
import allure
from endpoints.endpoint import Endpoint


class GetObjects(Endpoint):
    @allure.step('Get all objects')
    def get_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
