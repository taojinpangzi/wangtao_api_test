from pymysql import Connection
from config import *


class OperationsMYSQL:
    def __init__(self):
        self.connection = Connection(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            autocommit=True
        )

    # 执行查询性质的sql语句，返回查询结果
    def get_dql_result(self, db_name: str, sql_statement: str) -> tuple:
        self.connection.select_db(db_name)
        cursor = self.connection.cursor()
        cursor.execute(sql_statement)
        return cursor.fetchall()
