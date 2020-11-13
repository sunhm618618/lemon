"""
需要安装pymysql:  pip install pymysql
"""

import pymysql
from common.handle_config import conf


class MySQLHandler(object):
    """操作mysql数据库的类"""

    def __init__(self):
        """初始化方法中，连接到数据库"""
        # 建立连接
        self.con = pymysql.connect(host=conf.get("mysql", "host"),
                                   port=conf.getint("mysql", "port"),
                                   user=conf.get("mysql", "user"),
                                   password=conf.get("mysql", "password"),
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
        # 创建一个游标对象
        self.cur = self.con.cursor()

    def find_all(self, sql):
        """
        查询sql语句返回的所有数据
        :param sql: 查询的sql
        :return: 查询到的所有数据
        """
        self.con.commit()  # 提交事务， 为了同步数据。
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_one(self, sql):
        """
        查询sql语句返回的第一条数据
        :param sql: 查询的sql
        :type sql:str
        :return: sql语句查询到的第一条数据
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_count(self, sql):
        """
        sql语句查询到的数据条数
        :param sql: 查询的sql
        :return:查询到的数据条数
        """
        self.con.commit()
        res = self.cur.execute(sql)
        return res

    def update(self, sql):
        """
        增删改操作的方法
        :param sql: 增删改的sql语句
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        """断开游标，关闭连接"""
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    # 查所有注册的用户
    # sql = 'select * from futureloan.member;'
    db = MySQLHandler()
    # res = db.find_all(sql)
    # print(type(res))  # 返回一个list
    # print(res)
    sql = 'SELECT reg_name FROM futureloan.member where mobile_phone={}'.format('17817502435')
    print(sql)
    res = db.find_count(sql)  # 看有几个phone的记录
    print(res)
    db.close()
