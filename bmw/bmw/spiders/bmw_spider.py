# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem

class BmwSpiderSpider(scrapy.Spider):
    name = 'bmw_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    def parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            category = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()
            image_urls = uibox.xpath('.//ul/li/a/img/@src').getall()
            urls = list(map(lambda url:response.urljoin(url), image_urls))
            item = BmwItem(category=category, image_urls=urls)
            yield item
