from api.login import *
import pytest
import json
from config import *


def build_data(json_file: str) -> list:
    parametrize_data = list()
    with (open(json_file, "r", encoding="UTF-8") as f):
        for case_data in json.load(f):
            username = case_data["username"]
            password = case_data["password"]
            status = case_data["status"]
            code = case_data["code"]
            message = case_data["message"]
            parametrize_data.append((username, password, status, code, message))
    print(f"参数化数据{parametrize_data}")
    return parametrize_data


parametrize_data = build_data(BASE_PATH + "/data/parametrize_login.json")


class TestLoginAPI:
    uuid = None

    def setup_method(self):
        self.login_api = LoginAPI()
        get_verify_code_response = self.login_api.get_verify_code()
        TestLoginAPI.uuid = get_verify_code_response.json()["uuid"]

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("username, password, status, code, message", parametrize_data)
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
