from api.login import *
import pytest
from common.json_to_list import *
from config import *


class TestLoginAPI:
    uuid = None

    def setup_method(self):
        self.login_api = LoginAPI()
        get_verify_code_response = self.login_api.get_verify_code()
        TestLoginAPI.uuid = get_verify_code_response.json()["uuid"]

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("username, password, status, code, message", get_login_parametrize_data(DATA_PATH + "parametrize_login.json"))
    def test_parametrize_login(self, username, password, status, code, message):
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
