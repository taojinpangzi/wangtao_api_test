from pymysql import Connection
from config import *


# mysql数据库封装类
class OperationsMYSQL:
    def __init__(self):
        try:
            self.connection = Connection(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                autocommit=True
            )
        except Exception as e:
            print(f"数据库连接失败，原因是：{e}")

    # 执行查询性质的sql语句，返回查询结果
    def get_dql_result(self, db_name: str, sql_statement: str) -> tuple:
        try:
            cursor = self.connection.cursor()
            self.connection.select_db(db_name)
            cursor.execute(sql_statement)
            return cursor.fetchall()
        except Exception as e:
            print(f"数据库查询失败，原因是：{e}")


if __name__ == '__main__':
    op = OperationsMYSQL()
    print(op.get_dql_result("test", "select * from student"))
