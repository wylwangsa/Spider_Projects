import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider,Rule
from tencentcrawl.items import TencentcrawlItem


class TencentSpider(CrawlSpider):
	name='tencent'
	allow_domins=['hr.tencent.com']
	# url = 'http://hr.tencent.com/position.php?lid&start='
	hr_url = 'http://hr.tencent.com/'
	start_urls =['http://hr.tencent.com/position.php?lid&start=0']
	pagelink = LinkExtractor(allow=('start=\d+'))

	rules=[
		Rule(pagelink,callback='crawlTencent',follow=True)
	]
	def crawlTencent(self,response):
		for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
			item = TencentcrawlItem()
			type = each.xpath("./td[2]/text()").extract()
			if len(type) == 0:
				item['positiontype'] = '没有相关分类'
			else:
				item['positiontype'] =each.xpath("./td[2]/text()").extract()[0]
			item['positionlink'] = self.hr_url+each.xpath("./td[1]/a/@href").extract()[0]
			item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
			#item['positiontype'] = (each.xpath("./td[2]/text()").extract()[0] if each.xpath("./td[2]/text()").extract()[0] else None)
			#item['positiontype'] = each.xpath("./td[2]/text()").extract()
			item['positionnum']  = each.xpath("./td[3]/text()").extract()[0]
			item['positionaddr'] = each.xpath("./td[4]/text()").extract()[0]
			item['positiontime'] = each.xpath("./td[5]/text()").extract()[0]



			yield item