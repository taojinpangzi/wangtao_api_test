from api.course import *
from api.login import *


class TestAddCourse:
    uuid = None
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        response = self.login_api.get_verify_code()
        TestAddCourse.uuid = response.json()["uuid"]
        print(response.json()["uuid"])
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestAddCourse.uuid
        }
        response = self.login_api.login(test_data=login_data)
        TestAddCourse.token = response.json()["token"]
        print(TestAddCourse.token)

    def teardown_method(self):
        pass

    def test01_add_course_success(self):
        add_data = {
            "name": "测试开发提升课011111",
            "subject": "6",
            "price": 8991,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        }
        response = self.course_api.add_course(token=TestAddCourse.token, test_data=add_data)
        print(response.json())
        assert response.status_code == 200
        assert "成功" in response.text
        assert response.json()["code"] == 200

    def test01_add_course_fail(self):
        add_data = {
            "name": "测试开发提升课011111",
            "subject": "6",
            "price": 8991,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        }
        response = self.course_api.add_course(token="xxx", test_data=add_data)
        print(response.json())
        assert response.status_code == 200
        assert "失败" in response.text
        assert response.json()["code"] == 401
