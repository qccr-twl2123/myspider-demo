# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GirlItem(scrapy.Item):
    # 详情页
    detail_url = scrapy.Field()
    # 文章标题
    title = scrapy.Field()
    # 收录时间
    pick_up_time = scrapy.Field()
    # 头像链接
    image_url = scrapy.Field()
    # 浏览数
    view_number = scrapy.Field()
    # 回复数
    reply_number = scrapy.Field()
    # 主键Id
    user_id = scrapy.Field()
