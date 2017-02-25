# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeathercollectionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    date = scrapy.Field()
    daydesc = scrapy.Field()
    daytemp = scrapy.Field()
    wind = scrapy.Field()
    pm = scrapy.Field()
    air = scrapy.Field()
