from config import *


def get_parameter_login(uuid, username=USERNAME, password=PASSWORD):
    login_data = {
        "username": username,
        "password": password,
        "code": 2,
        "uuid": uuid
    }
    return login_data


def get_parameter_add_course(uuid, username=USERNAME, password=PASSWORD):
    add_course_data = {
        "username": username,
        "password": password,
        "code": 2,
        "uuid": uuid
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
