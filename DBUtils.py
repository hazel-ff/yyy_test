# 时间：2023/3/9 19:30
import logging

import pymysql
import pyodbc


class DBUtils:
    """
    连接数据库、创建游标
    """
    def __init__(self):
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
    关闭游标、连接
    """
    def colse(self):
        self.cursor.close()
        self.connt.close()


    """
    sql查询多条数据
    """
    def query_all(self,sql,params):
        try:
            # num表示执行sql查询的结果数
            num = self.cursor.execute(sql,params)
            # 将查询结果转为列表格式
            querydata = list(self.cursor.fetchall())
            index = []
            index_detail = self.cursor.description
            for i in index_detail:
                index.append()
            return
        except Exception as e:
            print("捕获到异常:",e)
        finally:
            self.colse()



    """
    sql查询单条数据
    """
    def query_one(self,sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()  # 数据【元组格式】
            index = self.get_index_dict(self.cursor)  # 字段名称【字典格式】
        except Exception as e:
            print("捕获到异常：",e)
        finally:
            pass


def query_log(type):
    sql = "select * from log where type = %(type)s"
    param = {"type":type}
    res = DBUtils().query_all(sql,param)
    return res



if __name__ == '__main__':
    print(query_log("auto' or '1'='1"))



