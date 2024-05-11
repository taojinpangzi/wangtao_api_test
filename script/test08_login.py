from api.login import *


class TestLoginAPI:

    uuid = None

    def setup_method(self):
        self.login_api = LoginAPI()
        response = self.login_api.get_verify_code()
        TestLoginAPI.uuid = response.json()["uuid"]
        print(response.json()["uuid"])

    def teardown_method(self):
        pass

    def test01_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        assert response.status_code == 200
        assert response.json()["code"] == 200
        assert "成功" in response.text

    def test02_without_username(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        assert response.status_code == 200
        assert response.json()["code"] == 500
        assert "错误" in response.text

    def test03_username_not_exist(self):
        login_data = {
            "username": "wangtao",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        assert response.status_code == 200
        assert response.json()["code"] == 500
        assert "错误" in response.text
