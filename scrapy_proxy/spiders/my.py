# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class MySpider(scrapy.Spider):
    name = 'my'
    allowed_domains = ['my.com']
    start_urls = ['http://ip.filefab.com/index.php']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={'proxy': 'https://165.227.169.12:80'})
        pass

    def parse(self, response):
        if response.status == 200:
            show = self.settings.get('SHOW_RESPONSE','None')
            if show == 'shell':
                from scrapy.shell import inspect_response
                inspect_response(response, self)
            elif show == 'browse':
                from scrapy.utils.response import open_in_browser
                open_in_browser(response)
            else:
                pass
        else:
            pass
        pass
