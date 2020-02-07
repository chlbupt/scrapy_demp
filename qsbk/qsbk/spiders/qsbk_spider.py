# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/p/6470213544?red_tag=m2637594212&traceid=']
    base_domain = 'http://tieba.baidu.com/'

    def parse(self, response):
        contentDivs = response.xpath("//div[@id='j_p_postlist']/div")
        for contentDiv in contentDivs:
            author = contentDiv.xpath('.//li[@class="d_name"]/a/text()').get()
            content = contentDiv.xpath('.//cc/div[2]/text()').get().strip()
            # print(author, content)
            # tieba = {'author': author, 'content' : content}
            item = QsbkItem(author=author, content=content)
            yield item

        next_url = response.xpath('//ul[@class="l_posts_num"]/li/a[last()-1]/@href').get()

        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain + next_url, self.parse)
