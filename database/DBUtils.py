# 时间：2023/3/9 19:30

import pymysql


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
    # def query_all(self,sql,params):
    #     try:
    #         # num表示执行sql查询的结果数
    #         num = self.cursor.execute(sql,params)
    #         # 将查询结果转为列表格式
    #         querydata = list(self.cursor.fetchall())
    #         index = []
    #         index_detail = self.cursor.description
    #         for i in index_detail:
    #             index.append()
    #         return
    #     except Exception as e:
    #         print("捕获到异常:",e)
    #     finally:
    #         self.colse()


    def query(self,sql):
        # 1、查数据；
        # 2、获取字段名；
        # 3、形成字典格式
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()    #查询到的数据,type:tuple
            name = self.cursor.description  #查询到的字段名，type:tuple
            result = {}   #存放最终一一对应的数据
            for element in name:
                for ele in data[0]:
                    result[element] = ele
            print(result)
            return result
        except Exception as e:
            print(f"捕获到异常……")
        finally:
            self.colse()


# def query_log(type):
#     sql = "select * from log where type = %(type)s"
#     param = {"type":type}
#     res = DBUtils().query_all(sql,param)
#     return res

if __name__ == '__main__':
    dbutils = DBUtils()
    dbutils.query("select * from test.student.grade where id=1")



