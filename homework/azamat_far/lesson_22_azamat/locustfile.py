from locust import task, HttpUser
import random


class Objects(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object', headers = {'Content-Type': 'application/json'}
        )

    @task(2)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.randrange(1, 7)}', headers = {'Content-Type': 'application/json'}
        )
