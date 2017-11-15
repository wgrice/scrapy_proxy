# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import scrapy

class MySQLExporterPipeline(object):

    insert_sql = "INSERT INTO proxy " \
                 "(protocol, ip, port, type) " \
                 "VALUES (%s, %s, %s, %s); "
    insert_sql_sapmle = "INSERT INTO proxy " \
                 "(protocol, ip, port, type) " \
                 "VALUES (0, '555.555.555.555', 5555, 0); "

    # 初始化数据库连接
    def __init__(self, conn, insert_num):
        self.conn = conn
        # 使用cursor()方法获取操作游标
        self.cursor = self.conn.cursor()
        self.items = []  # 缓存一定数目item后放入数据库

        self.insert_num = insert_num

    @classmethod
    def from_settings(cls, settings):

        host = settings['MYSQL_HOST'] # 读取settings中的配置
        port = settings['MYSQL_PORT']
        db = settings['MYSQL_DBNAME']
        user = settings['MYSQL_USER']
        passwd = settings['MYSQL_PASSWD']
        charset = 'utf8'  # 编码要加上，否则可能出现中文乱码问题

        insert_num = settings['ITEMS_ISNERT_TO_SQL_PER_TIME']

        # 打开数据库连接
        try:
            conn = pymysql.connect(host=host, port=port, user=user, password=passwd, database=db, charset=charset)
            return cls(conn, insert_num)  # 相当于dbpool付给了这个类，self中可以得到
        except Exception as e:
            print(e)

    def close_spider(self, spider):
        # 爬虫关闭时仍有 Item 未保存
        if len(self.items) > 0:
            self.insert_many()

        self.conn.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.items.append((item['protocol'], item['ip'], item['port'], item['type']))
        if len(self.items) >= self.insert_num:
            self.insert_many()

        return item

    def insert_many(self):
        try:
            # self.cursor.execute(self.insert_sql_sapmle)
            # self.cursor.execute(self.insert_sql, (item['protocol'], item['ip'], item['port'], item['type']))
            self.cursor.executemany(self.insert_sql, self.items)
            # 提交到数据库执行
            self.conn.commit()
            # 清空items
            self.items.clear()
        except Exception as e:
            # 如果发生错误则回滚
            self.conn.rollback()
            print(e)
