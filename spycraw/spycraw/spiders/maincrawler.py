#-*-coding:utf-8-*-
__author__ = 'liangz14'
# s
import scrapy
from spycraw.items import SpycrawItem
class Mycraw(scrapy.Spider):
    name='mycrawler'
    start_urls = [
        "http://www.qiushibaike.com/",
        "http://www.qiushibaike.com/",
        "http://www.qiushibaike.com/",
    ]

    def parse(self, response):
        yield SpycrawItem(a='a',b='b')
        print response.xpath('//div[@class="content"]').extract();

    def db_test(self):
        #from scrapy.shell import inspect_response
        #inspect_response(response,self)
        # 获取数据库 C.db_name
        # 获取表.C.db_name.collection_name;
        db = self.c.test;
        db.test.count*({'x':1})
        result = db.test.insert_one({"x":1})
        result.inserted_id
        db.test.find_one({"x":1})

        result = db.test.insert_many([{"x":1},{"x":2}])
        result.inserted_ids
