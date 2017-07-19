# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DongguanSpiderPipeline(object):
    def __init__(self):
        self.file_obj = open("dongguan.json", 'w')

    def process_item(self, item, spider):
        self.file_obj.write(json.dumps(dict(item),ensure_ascii=False).encode("utf-8") + "\n")
        return item

    def close_spider(self, spider):
        self.file_obj.close()