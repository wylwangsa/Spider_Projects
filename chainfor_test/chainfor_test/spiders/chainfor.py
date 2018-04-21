import scrapy
from scrapy import signals
from chainfor_test.items import ChainforTestItem
from scrapy.exceptions import CloseSpider

class ChainforSpider(scrapy.Spider):
	name = 'chainfor'
	allowd_domains =['https://www.chainfor.com/']
	#关键词
	keyword = '比特币'
	#start_urls =('https://www.chainfor.com/search/list/searchPage/data.do/type=1&pageNo=2&pageSize=20&keyWord=%E6%AF%94%E7%89%B9%E5%B8%81',)
	#加载并爬取索引内容，r抓包获取索引内容
	def start_requests(self):
		page = 1
		while True:
			#索引URL
			url = 'https://www.chainfor.com/search/list/searchPage/data.do'
			#格式化索引URL并自动加载下页
			yield scrapy.FormRequest(url=url,
			                            formdata={'type':'1','pageNo':str(page),'pageSize':'20','keyWord':self.keyword},
			                            callback=self.parse_page)
			page = page+1
	#通过索引页抓取每篇文章的URL
	def parse_page(self, response):
		#ids = response.xpath('//li[@class="m-news-stickTop-s cl"]')#.extract()
		#print(response.text)
		#获取详情页URL
		for id in response.xpath('//li[@class="m-news-stickTop-s cl"]'):
			url = id.xpath("./div[2]/h2/a/@href").extract()[0]
			yield scrapy.Request(url,callback=self.parse_detail_page)
	#通过获得的详情页URL，解析出URL地址，文章标题，带有图片地址的正文
	def parse_detail_page(self,response):
		item=ChainforTestItem()
		#过滤掉错误状态码的URL
		if response.status ==200:
			item['ID'] = response.url
			item['post_title'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/h1/text()').extract()[0]
			item['post_content'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]').extract()[0]

			#print(item['post_title'])
		else:
			pass

		yield item

