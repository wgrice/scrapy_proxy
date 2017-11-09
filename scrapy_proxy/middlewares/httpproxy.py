#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wgrice'
__mtime__ = '2017/11/7'
"""

from scrapy import signals
#project
from scrapy_proxy.util.util import Util


class ProxyMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler.settings)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        proxy = Util.get_proxy()
        spider.logger.info('Request proxy: %s' % proxy)
        request.meta['proxy'] = proxy

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

