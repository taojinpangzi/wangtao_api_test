from api.course import *
from api.login import *
from data.json_parameter import *


class TestDeleteCourse:
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        get_verify_code_response = self.login_api.get_verify_code()
        self.uuid = get_verify_code_response.json()["uuid"]
        print(self.uuid)

        login_response = self.login_api.login(test_data=get_parameter_login(self.uuid))
        TestDeleteCourse.token = login_response.json()["token"]
        print(TestDeleteCourse.token)

    def teardown_method(self):
        pass

    def test01_delete_course_success(self):
        response = self.course_api.delete_course(token=TestDeleteCourse.token, test_data=23056458704324889)
        assert response.status_code == 200
        assert "成功" in response.text
        assert response.json()["code"] == 200

    def test01_delete_course_fail(self):
        response = self.course_api.delete_course(token="xxx", test_data=30)
        assert response.status_code == 200
        assert "失败" in response.text
        assert response.json()["code"] == 401
