__author__ = 'liangz14'
# s
import scrapy
from pymongo import MongoClient

class Mycraw(scrapy.Spider):
    name='mycrawler'
    start_urls = [
        "http://www.qiushibaike.com/",
    ]
    c = MongoClient()

    def parse(self, response):

        print response.xpath('//div[@class="content"]').extract();

    def db_test(self):
        #from scrapy.shell import inspect_response
        #inspect_response(response,self)
        # ��ȡ���ݿ� C.db_name
        # ��ȡ��.C.db_name.collection_name;
        db = self.c.test;
        db.test.count*({'x':1})
        result = db.test.insert_one({"x":1})
        result.inserted_id
        db.test.find_one({"x":1})

        result = db.test.insert_many([{"x":1},{"x":2}])
        result.inserted_ids
