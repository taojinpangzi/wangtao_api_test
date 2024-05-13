import json


def get_login_parametrize_data(json_file: str) -> list[tuple]:
    parametrize_data = list()
    with (open(json_file, "r", encoding="UTF-8") as file):
        for dict_data in json.load(file):
            parametrize_data.append((dict_data["username"], dict_data["password"], dict_data["status"], dict_data["code"], dict_data["message"]))
    return parametrize_data
