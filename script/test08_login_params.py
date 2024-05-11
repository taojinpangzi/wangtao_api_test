from api.login import *
import pytest


test_data = [
    ("admin", "HM_2023_test", 200, 200, "成功"),
    ("", "HM_2023_test", 200, 500, "错误"),
    ("wangtao", "HM_2023_test", 200, 500, "错误")
]


class TestLoginAPI:

    uuid = None

    def setup_method(self):
        self.login_api = LoginAPI()
        response = self.login_api.get_verify_code()
        TestLoginAPI.uuid = response.json()["uuid"]
        print(response.json()["uuid"])

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("username, password, status, code, message", test_data)
    def test01_success(self, username, password, status, code, message):
        login_data = {
            "username": username,
            "password": password,
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        assert response.status_code == status
        assert response.json()["code"] == code
        assert message in response.text
