#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/11/7'
"""

import random

from scrapy_proxy.util.config import USER_AGENTS


class Util:

    @classmethod
    def get_user_agent(cls):
        return random.choice(USER_AGENTS)

    @classmethod
    def get_proxy(cls):
        pass


if __name__ == '__main__':
    print(Util.get_user_agent())
