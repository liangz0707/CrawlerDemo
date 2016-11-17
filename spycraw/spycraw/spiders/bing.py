# -*- coding:utf-8 -*-
__author__ = 'liangz14'
# s
import scrapy
import json
import scrapy
from spycraw.items import SpycrawItem
class Mycraw(scrapy.Spider):
    name='bing'
    start_urls = [
        "http://global.bing.com/search?q=%E6%9E%97%E4%B8%B9%E5%87%BA%E8%BD%A8"
    ]

    """
    def start_requests(self):
        print "调用start_requests"
        return [scrapy.Request("https://www.zhihu.com/" ,self.logged_in)]

    def logged_in(self,response):
        print "start_requests 的请求回调函数调用"
    """
    def parse(self, response):
        print "start_urls的回掉函数parse调用"
        item_list = response.xpath("//li[@class='b_algo']")
        for item in item_list:
            title = item.xpath("div[@class='b_title']/h2/a//text()").extract()
            title = "".join(title)
            link = item.xpath("div[@class='b_caption']/p/text()").extract()
            link = "".join(link)
            #print title,link
            yield SpycrawItem(title=title, link=link)

        url = response.xpath("//a[@title='Next page']/@href").extract()[0]
        url = response.urljoin(url)
        yield scrapy.Request(url,self.parse);

    def more_request(self, response):
        print "通过yield更多的请求"
