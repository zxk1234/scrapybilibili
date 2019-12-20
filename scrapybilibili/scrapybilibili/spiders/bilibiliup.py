# -*- coding: utf-8 -*-

from scrapy import Request,Spider
from urllib.parse import quote
from scrapybilibili.items import BilbiliItem, BilbiliupItem
import pandas as pd
from bs4 import BeautifulSoup
import re
import datetime
import pymongo

class BilibiliupSpider(Spider):
    name = 'bilibiliup'
    allowed_domains = ['space.bilibili.com']
    start_urls = ['https://space.bilibili.com/']
        
    def start_requests(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['bilibili']
        up_base_url='https://space.bilibili.com/'
        up_ids=self.db['video'].find({}, {'up_id':1, '_id':0})
        for i in up_ids:
            up_url=up_base_url+i['up_id']
            yield Request(url=up_url,callback=self.parse_up)

    def parse_up(self, response):
        '''
        解析用户信息
        :param response: response对象
        '''
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        bilibili_up_item=BilbiliupItem()
        #collection='up'
        bilibili_up_item['up_video_num'] = soup.select('#navigator > div > div.n-inner.clearfix > div.n-statistics > a.n-data.n-gz')[0].get('title')#Up 主总视频数
        bilibili_up_item['up_follow_num'] = ''.join(re.findall(r"\d+\.?\d*",soup.select('#navigator > div > div.n-inner.clearfix > div.n-statistics > a.n-data.n-fs')[0].get('title')))#Up 主总粉丝数
        bilibili_up_item['video_length'] = ''.join(re.findall(r"\d+\.?\d*",soup.select('#navigator > div > div.n-inner.clearfix > div.n-statistics > div')[0].get('title')))#Up 主总获赞数
        bilibili_up_item['created_at'] = ''.join(re.findall(r"\d+\.?\d*",soup.select('#navigator > div > div.n-inner.clearfix > div.n-statistics > div')[1].get('title')))#Up 主总播放数
        return bilibili_up_item