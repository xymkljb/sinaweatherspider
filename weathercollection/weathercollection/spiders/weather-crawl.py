# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from weathercollection.items import WeathercollectionItem


class Myspider(CrawlSpider):
    name = 'weather.sina.com.cn'
    allowed_domains = ['weather.sina.com.cn']
    start_urls = ['http://weather.sina.com.cn/china/']

    rules = (
        Rule(
            LinkExtractor(allow=r'/\w+sheng/$|/\w+shi/$|/\w+qu/$'),
            follow=True,
            callback='parse_item'),
             )

    def parse_item(self, response):
        self.log('Hi,this is an item page! %s' % response.url)

        item = WeathercollectionItem()
        print response.url.split('/')
        item['province'] = response.url.split('/')[-2]
        a = response.xpath('//td[@colspan="3"]/text()').extract()
        date = []
        for i in range(0, 3, 2):
            date.append(re.search(r'\(.*\)', a[i]).group()[1:-1]+a[i+1])
        item['date'] = date
        data = []
        for res in response.xpath('//div[@class="wd_cmain"]'):
            subdata = []
            subdata.append(
                res.xpath('.//div[@class="wd_cmh"]/text()').extract())
            subdata.append(res.css('td a::text').extract())
            subdata.append(res.css('p.wd_cmt_txt::text').extract())
            subdata.append(
                res.xpath('.//td[@style="width:125px;"]/text()').extract())
            data.append(subdata)
        item['data'] = data
        yield item
