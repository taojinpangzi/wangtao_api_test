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
