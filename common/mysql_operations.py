from pymysql import Connection
from config import *


class OperationsMYSQL:
    def __init__(self):
        self.connection = Connection(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            autocommit=False
        )

    # 获取游标对象
    def get_cursor(self, db_name: str):
        self.connection.select_db(db_name)
        return self.connection.cursor()
