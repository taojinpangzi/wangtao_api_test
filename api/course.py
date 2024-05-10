import requests


class AddCourseAPI:
    def __init__(self):
        self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"

    def add_course(self, token, test_data):
        return requests.post(url=self.url_add_course, headers={"Authorization": token}, json=test_data)
    