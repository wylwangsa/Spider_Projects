# -*- coding: utf-8 -*-
from taoshujutest.items import TaoshujuItem
from scrapy import Spider, FormRequest
import json

class taoshujuSpider(Spider):

    name = 'taoshuju'
    allowed_domains = ['taosj.com']
    word = '连衣裙'
    fields = 'word,pv,click,ctr,coverage,cpc,competition,catScore,levelStr,trendpv,searchTrend,recommend,catName,catFullName'
    refreshCache = 'false'
    url = 'http://www.taosj.com/restapi/train/sources/keywords/queryWordsData?word={}&fields={}&refreshCache={}'.format(word,fields,refreshCache)
    bs_url = 'http://www.taosj.com/restapi/train/sources/soaringWord?word={}&limit=10'.format(word)
    cookies = {
        'tencentSig': '',
        'uaid': '',
        'Hm_lvt_8c619410770b1c3446a04be9cfb938f7':'',
        'mjcc': '',
        '_qddamta_800098528': '',
        '_gat_UA - 103424414 - 1': '',
        'auth': '',
        '_qddaz': '',
        '_qdda': '',
        '_qddab': '',
        'Hm_lvt_cdfb35f92929b99ae60e80a03194be56': '',
        'Hm_lpvt_cdfb35f92929b99ae60e80a03194be56': '',
        '_ga': '',
        '_gid': ''
        }

    def start_requests(self):
        yield FormRequest(self.url, cookies=self.cookies, callback=self.parse)
        yield FormRequest(self.bs_url, cookies=self.cookies, callback=self.getcid_parse)

    def getcid_parse(self, response):
        print('---------')
        result = json.loads(response.text)
        for key in result['data']['wordsDataListMap']:
            '''http://www.taosj.com/restapi/train/sources/soaringWord/full?cid={}&limit=200&word2={}'''
            detail_url = 'http://www.taosj.com/restapi/train/sources/soaringWord/full?cid={}&limit=200&word2={}'
            if len(key) > 6:
                yield FormRequest(detail_url.format(key, self.word), cookies=self.cookies, callback=self.detail_parse)
        # cids = response.xpath('//*[@class="col-sm-4 col-md-4 word-soar-cloum"]/div[1]/div/a/attr["href"]').extract()[0]
        # for item in cids:
        #     print(item)
        #     print('---------')
        # print(cids)

    def detail_parse(self, response):
        result = json.loads(response.text)
        if 'data' in result:
            results=result['data']
            #print(results)
            item = TaoshujuItem()
            for wordsdata in results['wordsdatas']:
                item['avgClick'] = wordsdata['avgClick']
                item['avgCompetition'] = wordsdata['avgCompetition']
                item['avgCost'] = wordsdata['avgCost']
                item['avgCoverage'] = wordsdata['avgCoverage']
                item['avgCpc'] = wordsdata['avgCpc']
                item['avgCtr'] = wordsdata['avgCtr']
                item['avgDirectPay'] = wordsdata['avgDirectPay']
                item['avgDirectPayCount'] = wordsdata['avgDirectPayCount']
                item['avgFavItemCount'] = wordsdata['avgFavItemCount']
                item['avgFavShopCount'] = wordsdata['avgFavShopCount']
                item['avgFavtotal'] = wordsdata['avgFavtotal']
                item['avgIndirectPay'] = wordsdata['avgIndirectPay']
                item['avgIndirectPayCount'] = wordsdata['avgIndirectPayCount']
                item['avgPayCount'] = wordsdata['avgPayCount']
                item['avgPrice'] = wordsdata['avgPrice']
                item['avgPv'] = wordsdata['avgPv']
                item['avgRoi'] = wordsdata['avgRoi']
                item['avgSumPay'] = wordsdata['avgSumPay']
                item['avgRoi'] = wordsdata['avgRoi']
                item['trendpv'] = wordsdata['trendpv']
                item['searchTrend'] = wordsdata['searchTrend']
                item['cpc'] = wordsdata['cpc']
                item['coverage'] = wordsdata['coverage']
                item['click'] = wordsdata['click']
                item['word'] = wordsdata['word']
                item['pv'] = wordsdata['pv']
                item['ctr'] = wordsdata['ctr']
                item['competition'] =wordsdata['competition']
                item['catFullName'] = wordsdata['catFullName']
                item['catScoreDataPairList'] = wordsdata['catScoreDataPairList']
                item['catName'] = wordsdata['catName']
                item['detailWordsdataMap'] = wordsdata['detailWordsdataMap']
                item['fp'] = wordsdata['fp']
                item['historySumPv'] = wordsdata['historySumPv']
                item['hotTag'] = wordsdata['hotTag']
                item['keepTag'] = wordsdata['keepTag']
                item['lowPriceTag'] = wordsdata['lowPriceTag']
                item['maincat'] = wordsdata['maincat']
                item['testTag'] = wordsdata['testTag']

                yield item

    def parse(self, response):
        pass
        results = json.loads(response.text)
        #print('---------', results)
        if 'data' in results:
            result=results['data']
            dataresult = result['keywords']
            #print(dataresult)
            item = TaoshujuItem()
            for data in dataresult:
                #print(data)
                item['trendpv'] = data['trendpv']
                item['searchTrend'] = data['searchTrend']
                item['cpc'] = data['cpc']
                item['coverage'] = data['coverage']
                item['click'] = data['click']
                item['word'] = data['word']
                item['pv'] = data['pv']
                item['ctr'] = data['ctr']
                item['competition'] =data['competition']

                if len(data['catScore']) == 0:
                    item['catFullName'] = '-'
                    item['catScore']= '-'
                    item['catName'] = '-'
                else:
                    item['catFullName'] = data['catFullName']
                    item['catScore'] = data['catScore']
                    item['catName'] = data['catName']

                yield item



