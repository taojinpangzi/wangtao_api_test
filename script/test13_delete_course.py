from api.course import *
from api.login import *


class TestDeleteCourse:
    uuid = None
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        response = self.login_api.get_verify_code()
        TestDeleteCourse.uuid = response.json()["uuid"]
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestDeleteCourse.uuid
        }
        response = self.login_api.login(test_data=login_data)
        TestDeleteCourse.token = response.json()["token"]

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
