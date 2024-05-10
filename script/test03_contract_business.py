import pytest
from api.login import LoginAPI


class TestContractBusiness:
    # 前置处理
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()

    # 后置处理
    def teardown_method(self):
        pass

    # 登陆成功
    def test01_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        print(res_v.json()["uuid"])

        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json()["uuid"]
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
