# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json


class TaoshujuPipeline(object):

    def __init__(self):
        self.filename = open('E:\/newtaoshuju.json', 'wb')

    def process_item(self, item, spider):
        tsjtext = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(tsjtext.encode('utf-8'))

        return item

    def close_item(self):
        self.filename.close()

class NewtaoshujuPipeline(object):

    def __init__(self):
        self.filename =open('newtaoshuju.json', 'wb')

    def process_item(self):
        newtaoshujutext = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(newtaoshujutext.encode('utf-8'))

        return item

    def close_item(self):
        self.filename.close()
