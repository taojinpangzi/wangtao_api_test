import random
from config import *
from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI


class TestContractBusiness:
    token = None
    fileName = None

    # 前置处理
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        self.contract_api = ContractAPI()

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
        res_course = self.course_api.add_course(token=TestContractBusiness.token, test_data=add_data)
        print(res_course.status_code)
        print(res_course.json())

    # 上传合同成功
    def test03_upload_contract_success(self):
        upload_files = open(BASE_PATH + "/data/日本.txt", "r", encoding="UTF-8")
        res_contract = self.contract_api.upload_contract(token=TestContractBusiness.token, upload_files=upload_files)
        print(res_contract.status_code)
        print(res_contract.json())
        TestContractBusiness.fileName = res_contract.json()["fileName"]

    # 新增合同成功
    def test04_add_contract_success(self):
        contract_data = {
            "name": "测试888",
            "phone": "13612341888",
            "contractNo": f"HT20240501{random.randint(100000, 999999)}",
            "subject": "6",
            "courseId": 99,
            "channel": "0",
            "activityId": 77,
            "fileName": TestContractBusiness.fileName
        }
        res_add_contract = self.contract_api.add_contract(token=TestContractBusiness.token, add_contract_data=contract_data)
        print(res_add_contract.status_code)
        print(res_add_contract.json())
        assert (1, 2, 3) == (1, 2, 3)

