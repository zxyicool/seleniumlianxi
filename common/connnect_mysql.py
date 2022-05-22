# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/15 14:30
@Auth ： zxy
@File ：connnect_mysql.py

"""

import pymysql

# 配置数据库相关信息
dbinfo = {
    'host': '49.235.92.12',
    'user': 'root',
    'password': '123456',
    'port': 3309
}


class DbConnect():
    def __init__(self, db_cof, database=''):
        self.db_cof = db_cof
        # 打开数据库链接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方法获取游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # sql查询语句 list
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # sql删除，提交，修改语句
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


if __name__ == '__main__':
    db = DbConnect(dbinfo, 'online')
    sql1 = "select * from users_userprofile where username = '153234@qq.com'"
    result = db.select(sql1)
    print(result)





