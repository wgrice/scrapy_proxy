# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

class RefererMiddleware(object):
    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        if request.headers.has_key('Referer') and request.headers['Referer'] is not None:
            pass
        else:
            referer = request.meta['referer']
            spider.logger.info('Request referer: %s' % referer)
            request.headers['Referer'] = referer