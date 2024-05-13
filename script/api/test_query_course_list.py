from api.course import *
from api.login import *
from data.json_parameter import *
import re


class TestQueryCourseList:
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        get_verify_code_response = self.login_api.get_verify_code()
        self.uuid = get_verify_code_response.json()["uuid"]
        print(self.uuid)

        login_response = self.login_api.login(test_data=get_parameter_login(self.uuid))
        TestQueryCourseList.token = login_response.json()["token"]
        print(TestQueryCourseList.token)

    def teardown_method(self):
        pass

    def test01_select_course_success(self):
        add_data = "name=测试开发提升课01"
        response = self.course_api.query_course_list(token=TestQueryCourseList.token, test_data=add_data)
        assert response.status_code == 200
        assert response.json()["msg"] == "查询成功"
        assert response.json()["code"] == 200
        for rows in response.json()["rows"]:
            assert re.findall("测试开发提升课01", rows["name"])[0] == "测试开发提升课01"

    def test01_select_course_fail(self):
        add_data = "?name=测试开发提升课01"
        response = self.course_api.query_course_list(token="xxx", test_data=add_data)
        assert response.status_code == 200
        assert "失败" in response.text
        assert response.json()["code"] == 401
