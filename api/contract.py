import requests


class ContractAPI:
    def __init__(self):
        self.url_upload = "http://kdtx-test.itheima.net/api/common/upload"
        self.url_add_contract = "http://kdtx-test.itheima.net/api/contract"

    def upload_contract(self, upload_files, token):
        return requests.post(url=self.url_upload, files={"file": upload_files}, headers={"Authorization": token})

    def add_contract(self, add_contract_data, token):
        return requests.post(url=self.url_add_contract, json=add_contract_data, headers={"Authorization": token})

