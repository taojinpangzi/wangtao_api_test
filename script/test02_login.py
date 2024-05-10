import requests

url = "http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}
login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": 2,
    "uuid": "8e5f1bea63d2483e863f9353ffa69e35"
}

response = requests.post(url=url, headers=header_data, json=login_data)

print(response.status_code)
print(response.json())
