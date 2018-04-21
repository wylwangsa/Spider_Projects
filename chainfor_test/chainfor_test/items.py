# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class ChainforTestItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = Field()
    post_title = Field()
    post_content = Field()
    pass
