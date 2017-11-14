# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MySQLExporterPipeline(object):
    # 初始化数据库连接
    def __init__(self, conn):
        self.file = open('data/proxys.json', 'wb')

    @classmethod
    def from_settings(cls, settings):
        host = settings['MONGODB_HOST']
        conn = None
        return cls(conn)  # 相当于dbpool付给了这个类，self中可以得到

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
