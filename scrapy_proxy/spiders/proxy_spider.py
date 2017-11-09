# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

# project
from scrapy_proxy.items import ProxyItem
from scrapy_proxy.util.config import TEST_URL, TEST_IP_VISUAL, TEST_HTTP_HEADER, TEST_HTTPS_HEADER, PROXY_PARSER_LIST


class MySpider(scrapy.Spider):
    name = 'proxy_spider'
    allowed_domains = []
    start_urls = []

    def start_requests(self):
        for parser in PROXY_PARSER_LIST:
            parser_urls = parser['urls']
            for url in parser_urls:
                request = Request(url, callback=self.parse_page)
                request.meta['parser'] = parser
                yield request

        for url in self.start_urls:
            yield Request(url, callback=self.parse)
            # yield Request(url, callback=self.parse, meta={"proxy":"https://139.224.24.26:8888"})
        pass

    def parse(self, response):
        if response.status == 200:
            show = self.settings.get('SHOW_RESPONSE', 'None')
            if show == 'shell':
                from scrapy.shell import inspect_response
                inspect_response(response, self)
            elif show == 'browse':
                from scrapy.utils.response import open_in_browser
                open_in_browser(response)
            else:
                pass
        else:
            scrapy.Spider.log("Error code:" + response.status)
        pass

    def parse_page(self, response):
        parser = response.meta['parser']
        parser_type = parser['type']
        if parser_type == 'xpath':
            list = response.xpath(parser['pattern'])
            for row in list:
                yield self.parse_each_by_xpath(row, parser)
        elif parser_type == 'css':
            pass
        elif parser_type == 'module':  # 自定义模块
            pass
        else:
            scrapy.Spider.log("Error parser selector!")

    def parse_each_by_xpath(self, row, parser):
        item = ProxyItem()
        item['protocol'] = row.xpath(parser['position']['protocol']).extract_first().lower()
        item['ip'] = row.xpath(parser['position']['ip']).extract_first()
        item['port'] = row.xpath(parser['position']['port']).extract_first()
        item['type'] = row.xpath(parser['position']['type']).extract_first()
        item['country'] = row.xpath(parser['position']['country']).extract_first()
        item['area'] = row.xpath(parser['position']['area']).extract_first()
        item['speed'] = row.xpath(parser['position']['speed']).extract_first()
        return item

    def parse_each_by_css(self, i, parser):
        pass

    def parse_each_by_module(self, i, parser):
        pass
