# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .mysql import MysqlHelper


class BaikePipeline(object):
    mydb=None
    
    def __init__(self):
        self.mydb = MysqlHelper('192.168.0.107',3306,'root','123456','spider')

    def process_item(self, item, spider):
        try:
            self.mydb.insert('baidu_baike',{'title':item['title'],'url':item['url'],'content':item['content'],'tags':item['tags'],'attrs':item['attrs']})
        except:
            try:
                self.mydb = MysqlHelper('192.168.0.107',3306,'root','123456','spider')
            except:
                pass
            
