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
                 "VALUES (%d, %s, %d, %d); "

    # 初始化数据库连接
    def __init__(self, conn):
        self.conn = conn
        # 使用cursor()方法获取操作游标
        self.cursor = conn.cursor()

    @classmethod
    def from_settings(cls, settings):

        host = settings['MYSQL_HOST'] # 读取settings中的配置
        port = settings['MYSQL_PORT']
        db = settings['MYSQL_DBNAME']
        user = settings['MYSQL_USER']
        passwd = settings['MYSQL_PASSWD']
        charset = 'utf8'  # 编码要加上，否则可能出现中文乱码问题

        # 打开数据库连接
        try:
            conn = pymysql.connect(host=host, port=port, user=user, password=passwd, database=db, charset=charset)
            return cls(conn)  # 相当于dbpool付给了这个类，self中可以得到
        except Exception as e:
            print(e)


    def close_spider(self, spider):
        self.conn.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        try:
            self.cursor.execute(self.insert_sql, [item['protocol'], item['ip'], item['port'], item['type']])
        except Exception as e:
            print(e)
        return item
