# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from urllib.parse import quote
from scrapybilibili.items import BilbiliItem, BilbiliupItem
import pandas as pd
from bs4 import BeautifulSoup
import re
import datetime
import pymongo

class BilibiliSpider(Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://www.bilibili.com/']

    def start_requests(self):
        pd_url=pd.read_excel('/Users/apple/scrapybilibili/urls.xlsx',encoding='utf8')
        for i in pd_url['video_url ']:
            av_id=i.split('/')[-1][-13:-1]
            url=self.start_urls[0]+'video/'+av_id
            yield Request(url=url,callback=self.parse_video)

            
            
    def parse_video(self, response):
        '''
        解析视频信息
        :param response: response对象
        '''
        #self.logger.debug(response.text)
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        bilibili_item=BilbiliItem()
        bilibili_item['video_url']=response.url#视频地址
        bilibili_item['up_id']=soup.select('#v_upinfo > div.u-info > div.name > a.username')[0].get('href').split('/')[-1]#up 主 ID
        bilibili_item['up_username']=soup.select('#v_upinfo > div.u-info > div.name > a.username')[0].text#up 主用户名
        bilibili_item['video_url2']=soup.select('div.bilibili-player-video-wrap > div.bilibili-player-video > video')[0].get('src')#视频链接
        bilibili_item['video_name']=soup.select('#viewbox_report > h1 > span')[0].text#视频名称
        bilibili_item['video_published_at']=soup.select('#viewbox_report > div.video-data > span')[1].text#发布时间
        bilibili_item['video_playback_num']=re.findall(r"\d+\.?\d*",soup.select('#viewbox_report > div > span.view')[0].get('title'))[0]#视频播放量
        bilibili_item['video_barrage_num']=re.findall(r"\d+\.?\d*",soup.select('#viewbox_report > div > span.dm')[0].get('title'))[0]#弹幕量
        bilibili_item['video_like_num']=re.findall(r"\d+\.?\d*",soup.select('#arc_toolbar_report > div.ops > span.like')[0].get('title'))[0]#点赞量
        bilibili_item['video_coin_num']=re.findall(r"\d+\.?\d*",soup.select('#arc_toolbar_report > div.ops > span.coin')[0].get('title'))[0]#投币量
        bilibili_item['video_favorite_num']=re.findall(r"\d+\.?\d*",soup.select('#arc_toolbar_report > div.ops > span.collect')[0].get('title'))[0]#收藏量
        bilibili_item['video_forward_num']=re.findall(r"\d+\.?\d*", soup.select('#arc_toolbar_report > div.ops > span.share')[0].text)[0]#转发量
        bilibili_item['video_tag']=[i.text for i in soup.select('#v_tag > ul > li')]#视频标签
        bilibili_item['video_length']=soup.select('span.bilibili-player-video-time-total')[0].text#视频时长
        bilibili_item['created_at']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#爬取时间
        return bilibili_item
    