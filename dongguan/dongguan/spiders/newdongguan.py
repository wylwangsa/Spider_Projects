# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class NewdongguanSpider(CrawlSpider):
    name = 'newdongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']

    pagelinks = LinkExtractor(allow=('page=\d+'))
    detaillinks = LinkExtractor(allow=(r"http://wz.sun0769.com/html/question/\d+/\d+.shtml"))

    rules = [
        Rule(pagelinks,follow=True),
        Rule(detaillinks,callback='parse_item',follow=False)

    ]
    def detail_link(self,response):
        pass

    def parse_item(self, response):
        item = DongguanItem()
        item['title'] =response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract()[0]
        item['url'] = response.url
        image = response.xpath("/html/body/div[6]/div/div[2]/div[1]/div[1]/img/attr['src']").extract()

        if len(image) == 0:
            item['img'] = 'NULL'
            item['content']="".join(response.xpath('/html/body/div[6]/div/div[2]/div[1]/text()').extract()).strip()
            #print(item['img'])
        else:
            item['img'] =image[0]
            item['content'] = "".join(response.xpath('/html/body/div[6]/div/div[2]/div[1]/div[2]/text()').extract()).strip()
        #print(item['img'])
        #print(item['content'])
        yield item

