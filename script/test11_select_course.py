from api.course import *
from api.login import *
import re


class TestSelectCourse:
    uuid = None
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        response = self.login_api.get_verify_code()
        TestSelectCourse.uuid = response.json()["uuid"]
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestSelectCourse.uuid
        }
        response = self.login_api.login(test_data=login_data)
        TestSelectCourse.token = response.json()["token"]

    def teardown_method(self):
        pass

    def test01_select_course_success(self):
        add_data = "?name=测试开发提升课01"
        response = self.course_api.select_course(token=TestSelectCourse.token, test_data=add_data)
        assert response.status_code == 200
        assert response.json()["msg"] == "查询成功"
        assert response.json()["code"] == 200
        for rows in response.json()["rows"]:
            assert re.findall("测试开发提升课01", rows["name"])[0] == "测试开发提升课01"

    def test01_select_course_fail(self):
        add_data = "?name=测试开发提升课01"
        response = self.course_api.select_course(token="xxx", test_data=add_data)
        assert response.status_code == 200
        assert "失败" in response.text
        assert response.json()["code"] == 401
