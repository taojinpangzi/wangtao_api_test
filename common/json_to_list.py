import json
from typing import *


# 将json格式（list[dict]）的文本转化为list[list]
# *args为不定长参数，用以接收json格式中的字典key，组成元祖，通过args_data获取到元祖的每一个值，再通过value追加到args_list中，再追加到parametrize_data中
def get_login_parametrize_data(json_file: str, *args: str) -> list[list[Any]]:
    try:
        parametrize_data = list()
        with (open(json_file, "r", encoding="UTF-8") as file):
            for dict_data in json.load(file):
                args_list = list()
                for args_data in args:
                    args_list.append((dict_data[args_data]))
                parametrize_data.append(args_list)
        return parametrize_data
    except Exception as e:
        print(f"将json格式（list[dict]）的文本转化为list[list]时发生错误，原因是：{e}")


if __name__ == '__main__':
    print(get_login_parametrize_data("../data/parametrize_login.json", "username", "password", "status", "code", "message"))
