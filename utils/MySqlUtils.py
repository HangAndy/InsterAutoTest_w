#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   MySqlUtils
    Author:      Hang
    Date:        2020/4/15/015
    description: 数据库相关
   ==============================================

"""

import pymysql

from utils.LogUtil import log


class Mysql:
    def __init__(self, host, user, password, database, charset="utf8", port=3306):
        # 链接数据库
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )
        # 获取光标对象
        self.cursor = self.conn.cursor()
        # 导入日志
        self.log = self.log("MySqlUtils")

    def fetchone(self, sql: str):
        """
        查询方法， 获取一个结果
        :return: 查询到的结果
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql: str):
        """
        查询方法，获取多个结果
        :param sql: 查询sql语句
        :return:查询到的结果
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        """
        执行修改的方法
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.log.error("MySQL execution failed, rolled back！！")
            self.log.error(e)
            return False
        return True

    # 4、关闭对象（魔法方法，自动执行）
    def __del__(self):
        # 关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭连接对象
        if self.conn is not None:
            self.cursor.close()


if __name__ == '__main__':
    mysql = Mysql("127.0.0.1", "root", "hang", "hang")
    res = mysql.fetchone("select name, password from login")
    print(res)