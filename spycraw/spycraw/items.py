# -*- coding: utf-8 -*-

'''
这里主要用来，定义爬虫抛出的待处理数据
'''

import scrapy

class SpycrawItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
