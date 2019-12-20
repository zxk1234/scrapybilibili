# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field


class BilbiliItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection='video'
    video_url=Field()#视频地址
    up_id=Field()#up 主 ID
    up_username=Field()#up 主用户名
    video_url2=Field()#视频链接
    video_name=Field()#视频名称
    video_published_at=Field()#发布时间
    video_playback_num=Field()#视频播放量
    video_barrage_num=Field()#弹幕量
    video_like_num=Field()#点赞量
    video_coin_num=Field()#投币量
    video_favorite_num=Field()#收藏量
    video_forward_num=Field()#转发量
    video_tag=Field()#视频标签
    video_length=Field()#视频时长
    created_at=Field()#爬取时间

class BilbiliupItem(Item):
    collection='up'
    up_video_num = Field()#Up 主总视频数
    up_follow_num = Field()#Up 主总粉丝数
    video_length = Field()#Up 主总获赞数
    created_at = Field()#Up 主总播放数
