import requests
from config import *


class ContractAPI:
    def __init__(self):
        self.url_upload_contract = BASE_URL + "/api/common/upload"
        self.url_add_contract = BASE_URL + "/api/contract"
        self.url_query_contract_list = BASE_URL + "/api/contract/list"
        self.url_delete_contract = BASE_URL + " /api/contract/remove"

    def upload_contract(self, token, upload_file):
        return requests.post(url=self.url_upload_contract, headers={"Authorization": token}, files={"file": upload_file})

    def add_contract(self, token, test_data):
        return requests.post(url=self.url_add_contract, headers={"Authorization": token}, json=test_data)

    def query_contract_list(self, token, test_data):
        return requests.get(url=self.url_query_contract_list + f"?{test_data}", headers={"Authorization": token})

    def delete_contract(self, token, test_data):
        return requests.post(url=self.url_delete_contract, headers={"Authorization": token}, json=test_data)


