from api.course import *
from api.login import *
from data.json_parameter import *


class TestUpdateCourse:
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        get_verify_code_response = self.login_api.get_verify_code()
        self.uuid = get_verify_code_response.json()["uuid"]
        print(self.uuid)

        login_response = self.login_api.login(test_data=get_parameter_login(self.uuid))
        TestUpdateCourse.token = login_response.json()["token"]
        print(TestUpdateCourse.token)

    def teardown_method(self):
        pass

    def test01_update_course_success(self):
        update_data = {
            "id": 30,
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        response = self.course_api.update_course(token=TestUpdateCourse.token, test_data=update_data)
        assert response.status_code == 200
        assert "成功" in response.text
        assert response.json()["code"] == 200

    def test01_update_course_fail(self):
        update_data = {
            "id": 30,
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        response = self.course_api.update_course(token="xxx", test_data=update_data)
        assert response.status_code == 200
        assert "失败" in response.text
        assert response.json()["code"] == 401
