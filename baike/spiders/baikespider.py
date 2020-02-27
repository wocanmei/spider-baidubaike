# -*- coding: utf-8 -*-
import scrapy
import urllib
from lxml import html
from baike.items import BaikeItem

class baikespiderSpider(scrapy.Spider):
    name = 'baikespider'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['http://baike.baidu.com/']

    def parse(self, response):
        nexts = set(response.xpath("//a/@href").extract())
        for next in nexts:
            next_url = urllib.parse.urljoin(response.url, next)
            if('baike.baidu.com' in next_url):
                yield scrapy.Request(url=next_url, callback=self.parse)
        
        if('baike.baidu.com/item/' in response.url):
            try:
                title=response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()').extract()[0]
                contentt=response.xpath('//div[@class="main-content"]').xpath('string(.)').extract()
                content=contentt[0].strip().replace('\xa0','')
                attrs_name=response.xpath('//dt[@class="basicInfo-item name"]').xpath('string(.)').extract()
                attrs_value=response.xpath('//dd[@class="basicInfo-item value"]').xpath('string(.)').extract()
                attrs_name=[x.strip().replace('\xa0','') for x in attrs_name if True]
                attrs_value=[x.strip().replace('\xa0','') for x in attrs_value if True]
                # print(str(list(zip(attrs_name,attrs_value))))
                tags= response.xpath('//div[@id="open-tag"]/dd[@id="open-tag-item"]/span/text()').extract()
                tags=[x.strip().replace('\xa0','') for x in tags if x.strip()!='']

                item=BaikeItem()
                item['title']=title
                item['content']=content
                item['attrs']=str(list(zip(attrs_name,attrs_value)))
                item['tags']=str(tags)
                item['url']=response.url

                yield item

            except:
                pass
            

 

