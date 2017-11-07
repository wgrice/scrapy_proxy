#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/11/7'
"""

import unittest
import logging

from scrapy_proxy.util.util import Util

logger = logging.getLogger('util')

class TestUtil(unittest.TestCase):

    def setUp(self):
        logger.info('begin test.')
        pass

    def test_user_agent(self):
        logger.info('testing.')
        print(Util.get_user_agent())

    def tearDown(self):
        logger.info('end test.')
        pass