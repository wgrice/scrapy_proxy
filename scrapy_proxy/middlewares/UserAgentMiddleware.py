#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wgrice'
__mtime__ = '2017/11/7'
"""

from scrapy import signals
import random

class UserAgentMiddleware(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        agent = random.choice(self.agents)
        print(agent)
        request.headers.setdefault('User-Agent', agent)
