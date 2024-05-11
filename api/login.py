import requests
from config import *


class LoginAPI:
    # 初始化
    def __init__(self):
        self.url_verify = BASE_URL + "/api/captchaImage"
        self.url_login = BASE_URL + "/api/login"

    def get_verify_code(self):
        return requests.get(url=self.url_verify)

    def login(self, test_data):
        return requests.post(url=self.url_login, json=test_data)
