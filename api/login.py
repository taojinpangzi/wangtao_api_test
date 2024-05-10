import requests


class LoginAPI:
    # 初始化
    def __init__(self):
        self.url_verify = "http://kdtx-test.itheima.net/api/captchaImage"
        self.url_login = "http://kdtx-test.itheima.net/api/login"

    def get_verify_code(self):
        return requests.get(url=self.url_verify)

    def login(self, test_data):
        return requests.post(url=self.url_login, json=test_data)
