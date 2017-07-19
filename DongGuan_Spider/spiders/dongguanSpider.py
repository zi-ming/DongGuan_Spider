# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from DongGuan_Spider.items import DongguanSpiderItem

class DongguanspiderSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        # Rule(LinkExtractor(allow='type=4'),follow=True),
        # Rule(LinkExtractor(allow='page=\d+&type=4'), callback="parse_item_2", follow=False),
        Rule(LinkExtractor(allow='page=\d+$')),
        Rule(LinkExtractor(allow='\d+/\d+\.shtml'), callback='parse_item', follow=False),
    )

    # def parse_item_2(self, response):
    #     print(response.url)
    #     item = DongguanSpiderItem()
    #     item["link"] = response.url
    #     yield item

    def parse_item(self, response):
        item = DongguanSpiderItem()
        title_num = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        item["link"] = response.url
        item["title"] = title_num.split(u'  ')[0].split(u"：")[-1]
        item["num"] = title_num.split(u'  ')[1].split(u":")[-1]
        tmp =response.xpath('//div[@class="content text14_2"]//p[@class="te12h"]/text()').extract()[0].replace("'","").split()
        item["qus_date"] =  tmp[1].split(u"：")[-1] + " "+ tmp[2]
        item["status"] = response.xpath('//span[@class="qgrn"]/text()|//span[@class="qblue"]/text()|//span[@class="qred"]/text()').extract()[0]
        item["content"] = "".join(response.xpath('//div[@class="contentext"]/text()|//div[@class="c1 text14_2"]/text()').extract()).strip()
        yield item

