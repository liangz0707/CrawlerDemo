# -*-coding:utf-8-*-
__author__ = 'liangz14'
# s
import scrapy
from spycraw.items import SpycrawItem
import json

class Mycraw(scrapy.Spider):
    name='zhihu'
    start_urls = [
        "https://www.zhihu.com/#signin",
    ]

    def parse(self, response):
        #scrapy.FormRequest.from_response()
        return scrapy.FormRequest.from_response(
            response,
            formdata={"email":"603285292@qq.com","password":"love1314"},
            callback=self.after_login
            ,method="POST"
            ,url="https://www.zhihu.com/login/email"
        )

    def after_login(self, response):
        print response.body
        a = json.loads(response.body)
        print a["msg"]

        return scrapy.Request("https://www.zhihu.com/" ,self.parse_index)

    def parse_index(self,response):
        pass