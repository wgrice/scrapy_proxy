#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wgrice'
__mtime__ = '2017/11/7'
"""

from scrapy import signals
import random
#project
from scrapy_proxy.util.util import Util

class UserAgentMiddleware(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        agent = Util.get_user_agent()
        # spider.logger.info('Request User-Agent: %s' % agent)
        request.headers['User-Agent'] = agent
