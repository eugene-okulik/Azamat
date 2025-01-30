import requests
import allure
from endpoints.endpoint import Endpoint


class GetOneObject(Endpoint):
    @allure.step('Get one objects')
    def get_object(self, new_object, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/{new_object}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
