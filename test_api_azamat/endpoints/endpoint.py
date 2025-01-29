import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that name is same as sent')
    def check_response_title_correct(self, name):
        self.json = self.response.json()
        assert self.json['name'] == name

    @allure.step('Check_that_response_200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400

    @allure.step('Check count objects')
    def check_count_objects(self):
        assert len(self.json['data']) < 100, 'Not all objects'

    @allure.step('Check that post id is same')
    def check_id_object(self, new_object):
        assert self.json['id'] == new_object

    @allure.step('Check name change')
    def check_name_patch(self):
        assert self.json['name'] == 'New_name_object'
