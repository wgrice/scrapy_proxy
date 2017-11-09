#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/11/7'
"""

import random

from scrapy_proxy.util.config import USER_AGENTS
from scrapy_proxy.util.config import PROXYS


class Util:

    @classmethod
    def get_user_agent(cls):
        return random.choice(USER_AGENTS)

    @classmethod
    def get_user_agent_by_index(cls, index):
        return USER_AGENTS[index]

    @classmethod
    def get_proxy(cls):
        proxy = random.choice(PROXYS)
        protocol = proxy.get("protocol",None)
        ip = proxy.get("ip", None)
        port = proxy.get("port", None)
        return "%s://%s:%d" % (protocol, ip, port)

if __name__ == '__main__':
    print(Util.get_user_agent())
    print(Util.get_proxy())
