import requests


class CourseAPI:
    def __init__(self):
        self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"
        self.url_select_course = "http://kdtx-test.itheima.net/api/clues/course/list"

    def add_course(self, token, test_data):
        return requests.post(url=self.url_add_course, headers={"Authorization": token}, json=test_data)

    def select_course(self, token, test_data):
        return requests.get(url=self.url_select_course + f"/{test_data}", headers={"Authorization": token})
