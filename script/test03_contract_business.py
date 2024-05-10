import pytest
from api.login import LoginAPI


# 创建测试类
class TestContractBusiness:
    # 前置处理
    @pytest.fixture()
    def setup(self):
        # 实例化接口对象
        self.login_api = LoginAPI()

    # 后置处理
    @pytest.fixture()
    def teardown(self):
        pass

    # 登陆成功
    def test01_login_success(self, setup):
        pass

        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        print(res_v.json())

        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": "xxx"
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
