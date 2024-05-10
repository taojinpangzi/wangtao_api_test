import pytest
from api.login import LoginAPI
from api.course import CourseAPI


class TestContractBusiness:
    token = None

    # 前置处理
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.add_course_api = CourseAPI()

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
        TestContractBusiness.token = res_l.json()["token"]

    # 新增课程成功
    def test02_add_course_success(self):
        add_data = {
            "name": "测试开发提升课011111",
            "subject": "6",
            "price": 8991,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        }
        res_course = self.add_course_api.add_course(token=TestContractBusiness.token, test_data=add_data)
        print(res_course.status_code)
        print(res_course.json())
