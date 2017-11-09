# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProxyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class ProxyItem(scrapy.Item):
    # define the items of proxy
    source = scrapy.Field()  # 代理ip来源
    protocol = scrapy.Field()  # http or https or sock5
    ip = scrapy.Field()  # 地址
    port = scrapy.Field()  # 端口号
    type = scrapy.Field()  # 高匿 or 匿名 or 透明
    country = scrapy.Field()  # 国家
    area = scrapy.Field()  # 地区
    speed = scrapy.Field()  # 速度
    alive = scrapy.Field()  # 是否存活

