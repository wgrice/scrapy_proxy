# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from scrapy_proxy.spiders import crawl_item_num

class ItemCounterPipeline(object):

    def __init__(self):
        crawl_item_num = {}

    def close_spider(self, spider):
        # print(crawl_item_num)
        for key in crawl_item_num:
            spider.log("Spider:%s crawled %d item" % (key, crawl_item_num[key]))


    def process_item(self, item, spider):
        crawl_item_num[spider.name] = crawl_item_num.setdefault(spider.name, 0) + 1
        return item
