from common.data_handle import *
from config import *


def get_parameter_login(uuid, username=USERNAME, password=PASSWORD, code=VERIFY_CODE):
    login_data = {
        "username": username,
        "password": password,
        "code": code,
        "uuid": uuid
    }
    return login_data


def get_parameter_add_course(name=f"测试课程{get_date_random_number()}", subject="6", price=1000,
                             applicablePerson="2", info="测试信息"):
    add_course_data = {
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson": applicablePerson,
            "info": info
    }
    return add_course_data


def get_parameter_update_course(uuid, username=USERNAME, password=PASSWORD):
    update_course_data = {
        "username": username,
        "password": password,
        "code": 2,
        "uuid": uuid
    }
    return update_course_data


def get_parameter_add_contract(uuid, username=USERNAME, password=PASSWORD):
    add_contract_data = {
        "username": username,
        "password": password,
        "code": 2,
        "uuid": uuid
    }
    return add_contract_data


def get_parameter_delete_contract(uuid, username=USERNAME, password=PASSWORD):
    delete_contract_data = {
        "username": username,
        "password": password,
        "code": 2,
        "uuid": uuid
    }
    return delete_contract_data
