# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient


class MongoDBExporterPipeline(object):
    # 初始化数据库连接
    def __init__(self, client):
        self.client = client
        self.db = self.client.spider
        self.collection = self.db.proxy
        self.items = []  # 缓存一定数目item后放入数据库

    @classmethod
    def from_settings(cls, settings):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        try:
            client = MongoClient('localhost', 27017)
            return cls(client)  # 相当于dbpool付给了这个类，self中可以得到
        except Exception as e:
            pass

    def close_spider(self, spider):
        self.client.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        insert = dict(item)
        self.items.append(insert)
        if len(self.items) >= 10:
            try:
                # self.collection.insert_one(insert)
                self.collection.insert_many(self.items)

                self.items.clear()
            except Exception as e:
                pass

        return item
