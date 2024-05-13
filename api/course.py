import requests
from config import *


class CourseAPI:
    def __init__(self):
        # 新增/修改/删除课程的url一致
        self.url_add_course = BASE_URL + "/api/clues/course"
        self.url_query_course_list = BASE_URL + "/api/clues/course/list"

    def add_course(self, token, test_data):
        return requests.post(url=self.url_add_course, headers={"Authorization": token}, json=test_data)

    def query_course_list(self, token, test_data):
        return requests.get(url=self.url_query_course_list + f"?{test_data}", headers={"Authorization": token})

    def delete_course(self, token, test_data):
        return requests.delete(url=self.url_add_course + f"/{test_data}", headers={"Authorization": token})

    def update_course(self, token, test_data):
        return requests.put(url=self.url_add_course, headers={"Authorization": token}, json=test_data)
