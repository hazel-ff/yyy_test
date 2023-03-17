# 时间：2023/3/9 19:30
import pymysql
import pyodbc


class DBUtils:
     def __init__(self):
         # 连接数据库、创建游标
         # self.connt = pyodbc.connect(
         #
         # )
         self.connt = pymysql.connect(
            user="root",
            password="yangmysql1",
            db="mysql",
            host="localhost",
            port=3306

         )
         self.cursor = self.connt.cursor()


     """
     关闭连接
     """
     def colse(self):
         self.cursor.close()
         self.connt.close()

     """
     sql查询语句
     """
     def query_one(self,sql,param):
         try:
             self.cursor.execute(sql,param)
             return self.cursor.fetchone()
         except Exception as e:
             print("捕获到异常",e)
         finally:
             self.cursor.close()


def query_all(id):
    sql = "select * from log where id=%(i_d)s"
    param = {"i_d":id}
    res = DBUtils().query_one(sql,param)
    return res


if __name__ == '__main__':
    print(query_all(3))


