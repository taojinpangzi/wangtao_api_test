import requests
from data.json_parameter import *

url = "http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=header_data, json=get_parameter_login("8e5f1bea63d2483e863f9353ffa69e35"))

print(response.status_code)
print(response.json())
