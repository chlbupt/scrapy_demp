# -*- coding: utf-8 -*-
import scrapy


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):

        url = 'http://www.renren.com/PLogin.do'
        data = {'email': '18001351215@163.com', 'password': 'aa590702'}
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        profile_url = 'http://www.renren.com/880151247/profile'
        request = scrapy.Request(profile_url, callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open('profile.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)