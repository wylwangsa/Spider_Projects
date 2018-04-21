# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from chainfor_test.items import ChainforTestItem
from scrapy.exceptions import DropItem
import json

def getdbconn():
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='123456',
                           db='',
                           charset='utf8'
                           )
    return conn



class ChainforTestPipeline(object):
    def __init__(self):
        self.ids_seen = set()
    def process_item(self, item, spider):
        if item['ID']  in self.ids_seen:
            raise DropItem("元素重复:%s"%item)
        else:
            self.ids_seen.add(item['ID'])
            if item.__class__ ==ChainforTestItem:
                self.insert(item)
                return
        return item

    def insert(self,item):

        conn = getdbconn()
        cursor=conn.cursor()
        sql = "insert into wp_posts(id,posts_title,posts_content)VALUES(%s,%s,%s)"
        params =(item['ID'],item['post_title'],item['post_content'])
        cursor.execute(sql,params)

        conn.commit()
        cursor.close()
        conn.close()

