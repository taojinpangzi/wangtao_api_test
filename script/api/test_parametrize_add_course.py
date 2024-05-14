from api.login import *
from api.course import *
from data.json_parameter import *
import pytest
from common.json_to_list import *
from common.data_handle import *
from config import *


class TestAddCourseAPI:
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        get_verify_code_response = self.login_api.get_verify_code()
        self.uuid = get_verify_code_response.json()["uuid"]
        print(self.uuid)

        login_response = self.login_api.login(test_data=get_parameter_login(self.uuid))
        TestAddCourseAPI.token = login_response.json()["token"]
        print(TestAddCourseAPI.token)

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("name, subject, price, applicablePerson, info, status, code, message",
                             get_login_parametrize_data(DATA_PATH + "parametrize_add_course.json", "name", "subject", "price", "applicablePerson", "info", "status", "code", "message"))
    def test_parametrize_add_course(self, name, subject, price, applicablePerson, info, status, code, message):
        add_course_data = {
            "name": f"{name}{get_date_random_number()}",
            "subject": subject,
            "price": price,
            "applicablePerson": applicablePerson,
            "info": info
        }
        response = self.course_api.add_course(token=TestAddCourseAPI.token, test_data=add_course_data)
        assert response.status_code == status
        assert response.json()["code"] == code
        assert message in response.text
