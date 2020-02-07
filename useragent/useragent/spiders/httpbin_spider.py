# -*- coding: utf-8 -*-
import scrapy
from json import loads

class HttpbinSpiderSpider(scrapy.Spider):
    name = 'httpbin_spider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        print('='*30)
        userAgent = loads(response.text)['user-agent']
        print(userAgent)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
