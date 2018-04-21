# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionname = scrapy.Field()
    positionlink = scrapy.Field()
    positiontype = scrapy.Field()
    positionnum = scrapy.Field()
    positionaddr = scrapy.Field()
    positiontime = scrapy.Field()