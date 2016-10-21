__author__ = 'liangz14'

import scrapy

class Mycraw(scrapy.Spider):
    name='mycrawler'
    start_urls = [
        "http://www.qiushibaike.com/",
    ]

    def parse(self, response):
        print response.xpath('//div[@class="content"]').extract();