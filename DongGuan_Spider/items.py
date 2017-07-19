# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanSpiderItem(scrapy.Item):
    link = scrapy.Field()           # 投诉链接
    title = scrapy.Field()          # 投诉标题
    content = scrapy.Field()       # 投诉内容
    num = scrapy.Field()            # 投诉编号
    qus_date = scrapy.Field()       # 投诉日期
    status = scrapy.Field()         # 处理状态
