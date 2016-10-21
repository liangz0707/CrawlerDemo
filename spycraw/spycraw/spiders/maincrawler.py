__author__ = 'liangz14'
# s
import scrapy

class Mycraw(scrapy.Spider):
    name='mycrawler'
    start_urls = [
        "http://www.qiushibaike.com/",
    ]

    def parse(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response,self)
        print response.xpath('//div[@class="content"]').extract();