# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import GirlItem
from lxml import etree
from bs4 import BeautifulSoup
import re
import traceback
import os
from pathlib import Path
import urllib.request
import requests


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['19lou.com']
    # start_urls = ["https://www.19lou.com/r/1/19lnsxq-10.html",
    #               "https://www.19lou.com/r/1/19lnsxq-11.html",
    #               "https://www.19lou.com/r/1/19lnsxq-12.html",
    #               "https://www.19lou.com/r/1/19lnsxq-13.html",
    #               "https://www.19lou.com/r/1/19lnsxq-14.html",
    #               "https://www.19lou.com/r/1/19lnsxq-15.html",
    #               "https://www.19lou.com/r/1/19lnsxq-16.html",
    #               "https://www.19lou.com/r/1/19lnsxq-17.html",
    #               "https://www.19lou.com/r/1/19lnsxq-18.html",
    #               "https://www.19lou.com/r/1/19lnsxq-19.html",
    #               "https://www.19lou.com/r/1/19lnsxq-20.html",
    #               "https://www.19lou.com/r/1/19lnsxq-21.html",
    #               "https://www.19lou.com/r/1/19lnsxq-22.html",
    #               "https://www.19lou.com/r/1/19lnsxq-23.html",
    #               "https://www.19lou.com/r/1/19lnsxq-24.html",
    #               "https://www.19lou.com/r/1/19lnsxq-25.html",
    #               "https://www.19lou.com/r/1/19lnsxq-26.html",
    #               "https://www.19lou.com/r/1/19lnsxq-27.html",
    #               "https://www.19lou.com/r/1/19lnsxq-28.html",
    #               "https://www.19lou.com/r/1/19lnsxq-29.html",
    #               "https://www.19lou.com/r/1/19lnsxq-30.html",
    #               "https://www.19lou.com/r/1/19lnsxq-31.html",
    #               "https://www.19lou.com/r/1/19lnsxq-32.html",
    #               "https://www.19lou.com/r/1/19lnsxq-33.html",
    #               "https://www.19lou.com/r/1/19lnsxq-34.html",
    #               "https://www.19lou.com/r/1/19lnsxq-35.html",
    #               "https://www.19lou.com/r/1/19lnsxq-36.html",
    #               "https://www.19lou.com/r/1/19lnsxq-37.html",
    #               "https://www.19lou.com/r/1/19lnsxq-38.html"]
    start_urls = ['https://www.19lou.com/r/1/19lnsxq-39.html', 'https://www.19lou.com/r/1/19lnsxq-40.html', 'https://www.19lou.com/r/1/19lnsxq-41.html', 'https://www.19lou.com/r/1/19lnsxq-42.html', 'https://www.19lou.com/r/1/19lnsxq-43.html', 'https://www.19lou.com/r/1/19lnsxq-44.html', 'https://www.19lou.com/r/1/19lnsxq-45.html', 'https://www.19lou.com/r/1/19lnsxq-46.html', 'https://www.19lou.com/r/1/19lnsxq-47.html', 'https://www.19lou.com/r/1/19lnsxq-48.html', 'https://www.19lou.com/r/1/19lnsxq-49.html', 'https://www.19lou.com/r/1/19lnsxq-50.html', 'https://www.19lou.com/r/1/19lnsxq-51.html', 'https://www.19lou.com/r/1/19lnsxq-52.html', 'https://www.19lou.com/r/1/19lnsxq-53.html', 'https://www.19lou.com/r/1/19lnsxq-54.html', 'https://www.19lou.com/r/1/19lnsxq-55.html', 'https://www.19lou.com/r/1/19lnsxq-56.html', 'https://www.19lou.com/r/1/19lnsxq-57.html', 'https://www.19lou.com/r/1/19lnsxq-58.html', 'https://www.19lou.com/r/1/19lnsxq-59.html', 'https://www.19lou.com/r/1/19lnsxq-60.html', 'https://www.19lou.com/r/1/19lnsxq-61.html', 'https://www.19lou.com/r/1/19lnsxq-62.html', 'https://www.19lou.com/r/1/19lnsxq-63.html', 'https://www.19lou.com/r/1/19lnsxq-64.html', 'https://www.19lou.com/r/1/19lnsxq-65.html', 'https://www.19lou.com/r/1/19lnsxq-66.html', 'https://www.19lou.com/r/1/19lnsxq-67.html', 'https://www.19lou.com/r/1/19lnsxq-68.html', 'https://www.19lou.com/r/1/19lnsxq-69.html', 'https://www.19lou.com/r/1/19lnsxq-70.html', 'https://www.19lou.com/r/1/19lnsxq-71.html', 'https://www.19lou.com/r/1/19lnsxq-72.html', 'https://www.19lou.com/r/1/19lnsxq-73.html', 'https://www.19lou.com/r/1/19lnsxq-74.html', 'https://www.19lou.com/r/1/19lnsxq-75.html', 'https://www.19lou.com/r/1/19lnsxq-76.html', 'https://www.19lou.com/r/1/19lnsxq-77.html', 'https://www.19lou.com/r/1/19lnsxq-78.html', 'https://www.19lou.com/r/1/19lnsxq-79.html', 'https://www.19lou.com/r/1/19lnsxq-80.html', 'https://www.19lou.com/r/1/19lnsxq-81.html', 'https://www.19lou.com/r/1/19lnsxq-82.html', 'https://www.19lou.com/r/1/19lnsxq-83.html', 'https://www.19lou.com/r/1/19lnsxq-84.html', 'https://www.19lou.com/r/1/19lnsxq-85.html', 'https://www.19lou.com/r/1/19lnsxq-86.html', 'https://www.19lou.com/r/1/19lnsxq-87.html', 'https://www.19lou.com/r/1/19lnsxq-88.html', 'https://www.19lou.com/r/1/19lnsxq-89.html', 'https://www.19lou.com/r/1/19lnsxq-90.html', 'https://www.19lou.com/r/1/19lnsxq-91.html', 'https://www.19lou.com/r/1/19lnsxq-92.html', 'https://www.19lou.com/r/1/19lnsxq-93.html', 'https://www.19lou.com/r/1/19lnsxq-94.html', 'https://www.19lou.com/r/1/19lnsxq-95.html', 'https://www.19lou.com/r/1/19lnsxq-96.html', 'https://www.19lou.com/r/1/19lnsxq-97.html', 'https://www.19lou.com/r/1/19lnsxq-98.html', 'https://www.19lou.com/r/1/19lnsxq-99.html', 'https://www.19lou.com/r/1/19lnsxq-100.html', 'https://www.19lou.com/r/1/19lnsxq-101.html', 'https://www.19lou.com/r/1/19lnsxq-102.html', 'https://www.19lou.com/r/1/19lnsxq-103.html', 'https://www.19lou.com/r/1/19lnsxq-104.html', 'https://www.19lou.com/r/1/19lnsxq-105.html', 'https://www.19lou.com/r/1/19lnsxq-106.html', 'https://www.19lou.com/r/1/19lnsxq-107.html', 'https://www.19lou.com/r/1/19lnsxq-108.html', 'https://www.19lou.com/r/1/19lnsxq-109.html', 'https://www.19lou.com/r/1/19lnsxq-110.html', 'https://www.19lou.com/r/1/19lnsxq-111.html', 'https://www.19lou.com/r/1/19lnsxq-112.html', 'https://www.19lou.com/r/1/19lnsxq-113.html', 'https://www.19lou.com/r/1/19lnsxq-114.html', 'https://www.19lou.com/r/1/19lnsxq-115.html', 'https://www.19lou.com/r/1/19lnsxq-116.html', 'https://www.19lou.com/r/1/19lnsxq-117.html', 'https://www.19lou.com/r/1/19lnsxq-118.html', 'https://www.19lou.com/r/1/19lnsxq-119.html', 'https://www.19lou.com/r/1/19lnsxq-120.html', 'https://www.19lou.com/r/1/19lnsxq-121.html', 'https://www.19lou.com/r/1/19lnsxq-122.html', 'https://www.19lou.com/r/1/19lnsxq-123.html', 'https://www.19lou.com/r/1/19lnsxq-124.html', 'https://www.19lou.com/r/1/19lnsxq-125.html', 'https://www.19lou.com/r/1/19lnsxq-126.html', 'https://www.19lou.com/r/1/19lnsxq-127.html', 'https://www.19lou.com/r/1/19lnsxq-128.html', 'https://www.19lou.com/r/1/19lnsxq-129.html', 'https://www.19lou.com/r/1/19lnsxq-130.html', 'https://www.19lou.com/r/1/19lnsxq-131.html', 'https://www.19lou.com/r/1/19lnsxq-132.html', 'https://www.19lou.com/r/1/19lnsxq-133.html', 'https://www.19lou.com/r/1/19lnsxq-134.html', 'https://www.19lou.com/r/1/19lnsxq-135.html', 'https://www.19lou.com/r/1/19lnsxq-136.html', 'https://www.19lou.com/r/1/19lnsxq-137.html', 'https://www.19lou.com/r/1/19lnsxq-138.html', 'https://www.19lou.com/r/1/19lnsxq-139.html', 'https://www.19lou.com/r/1/19lnsxq-140.html', 'https://www.19lou.com/r/1/19lnsxq-141.html', 'https://www.19lou.com/r/1/19lnsxq-142.html', 'https://www.19lou.com/r/1/19lnsxq-143.html', 'https://www.19lou.com/r/1/19lnsxq-144.html', 'https://www.19lou.com/r/1/19lnsxq-145.html', 'https://www.19lou.com/r/1/19lnsxq-146.html', 'https://www.19lou.com/r/1/19lnsxq-147.html', 'https://www.19lou.com/r/1/19lnsxq-148.html', 'https://www.19lou.com/r/1/19lnsxq-149.html', 'https://www.19lou.com/r/1/19lnsxq-150.html', 'https://www.19lou.com/r/1/19lnsxq-151.html', 'https://www.19lou.com/r/1/19lnsxq-152.html', 'https://www.19lou.com/r/1/19lnsxq-153.html', 'https://www.19lou.com/r/1/19lnsxq-154.html', 'https://www.19lou.com/r/1/19lnsxq-155.html', 'https://www.19lou.com/r/1/19lnsxq-156.html', 'https://www.19lou.com/r/1/19lnsxq-157.html', 'https://www.19lou.com/r/1/19lnsxq-158.html', 'https://www.19lou.com/r/1/19lnsxq-159.html', 'https://www.19lou.com/r/1/19lnsxq-160.html', 'https://www.19lou.com/r/1/19lnsxq-161.html', 'https://www.19lou.com/r/1/19lnsxq-162.html', 'https://www.19lou.com/r/1/19lnsxq-163.html', 'https://www.19lou.com/r/1/19lnsxq-164.html', 'https://www.19lou.com/r/1/19lnsxq-165.html', 'https://www.19lou.com/r/1/19lnsxq-166.html', 'https://www.19lou.com/r/1/19lnsxq-167.html', 'https://www.19lou.com/r/1/19lnsxq-168.html', 'https://www.19lou.com/r/1/19lnsxq-169.html', 'https://www.19lou.com/r/1/19lnsxq-170.html', 'https://www.19lou.com/r/1/19lnsxq-171.html', 'https://www.19lou.com/r/1/19lnsxq-172.html', 'https://www.19lou.com/r/1/19lnsxq-173.html', 'https://www.19lou.com/r/1/19lnsxq-174.html', 'https://www.19lou.com/r/1/19lnsxq-175.html', 'https://www.19lou.com/r/1/19lnsxq-176.html', 'https://www.19lou.com/r/1/19lnsxq-177.html', 'https://www.19lou.com/r/1/19lnsxq-178.html', 'https://www.19lou.com/r/1/19lnsxq-179.html', 'https://www.19lou.com/r/1/19lnsxq-180.html', 'https://www.19lou.com/r/1/19lnsxq-181.html', 'https://www.19lou.com/r/1/19lnsxq-182.html', 'https://www.19lou.com/r/1/19lnsxq-183.html', 'https://www.19lou.com/r/1/19lnsxq-184.html', 'https://www.19lou.com/r/1/19lnsxq-185.html', 'https://www.19lou.com/r/1/19lnsxq-186.html', 'https://www.19lou.com/r/1/19lnsxq-187.html', 'https://www.19lou.com/r/1/19lnsxq-188.html', 'https://www.19lou.com/r/1/19lnsxq-189.html', 'https://www.19lou.com/r/1/19lnsxq-190.html', 'https://www.19lou.com/r/1/19lnsxq-191.html', 'https://www.19lou.com/r/1/19lnsxq-192.html', 'https://www.19lou.com/r/1/19lnsxq-193.html', 'https://www.19lou.com/r/1/19lnsxq-194.html', 'https://www.19lou.com/r/1/19lnsxq-195.html', 'https://www.19lou.com/r/1/19lnsxq-196.html', 'https://www.19lou.com/r/1/19lnsxq-197.html', 'https://www.19lou.com/r/1/19lnsxq-198.html', 'https://www.19lou.com/r/1/19lnsxq-199.html']
    start_urls = start_urls[131: 170]
    # with open(os.path.join(Path(__file__).parent, 'urls.txt'), 'r') as f:
    #     start_url_list = f.readlines()
    #     for url in start_url_list:
    #         start_urls.append(url)
    # print(start_urls)
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }

    def parse(self, response):
        html = etree.HTML(response.text, parser=etree.HTMLParser(encoding='gb18030'))
        div_elements = html.xpath('.//*[@class="J_item J_toUrl item item-a"]')

        for div_element in div_elements:
            detail_url = self.extract_detail_url(div_element)
            title = self.extract_title(div_element)[0]
            pick_up_time = self.extract_pick_up_time(div_element)[0]
            image_url = self.extract_image_url(div_element)
            view_number, reply_number = self.extract_views_and_reply_number(div_element)
            user_id = self.extract_user_id(div_element)

            girl_item = GirlItem(detail_url=detail_url, title=title, user_id=user_id,
                                 pick_up_time=pick_up_time, image_url=image_url, view_number=view_number,
                                 reply_number=reply_number)
            print(image_url)
            data = requests.get(image_url).content
            with open('/Users/mac/Documents/document/girl2/' + str(user_id) + '.jpg', 'wb') as f:
                f.write(data)
            # url = 'https://www.python.org/static/img/python-logo.png'
            # urllib.request.urlretrieve(url, "logo1.png")
            # urllib.request.urlretrieve(image_url, '/Users/mac/Documents/document/images/' + str(user_id) + '.jpg')
            yield girl_item

    @staticmethod
    def extract_detail_url(item_html):
        detail_url = item_html.xpath('./@data-url')[0]
        if detail_url is None:
            raise Exception('can not find detail url')
        return detail_url

    @staticmethod
    def extract_title(item_html):
        title = item_html.xpath('./div[@class="item-hd"]/h3/text()')
        if title is None:
            raise Exception('extract title exception')
        return title

    @staticmethod
    def extract_pick_up_time(item_html):
        pick_up_time = item_html.xpath('./div[@class="item-hd"]/p/text()')
        if pick_up_time is None:
            raise Exception('pick up time exception')
        return pick_up_time

    @staticmethod
    def extract_user_id(item_html):
        user_id = item_html.xpath("./@data-btid")[0]
        return user_id

    @staticmethod
    def extract_image_url(item_html):
        image_url = item_html.xpath('./div[@class="item-bd"]/div[@class="pics"]/img/@data-src')[0]  # 先找到所有的img
        if image_url is None:
            raise Exception('imgage url exception')
        return image_url

    def download_schedule(blocknum, blocksize, totalsize):
        per = 100.0 * blocknum * blocksize / totalsize
        if per > 100:
            return per
        print('当前下载进度 %d ' % per)

    @staticmethod
    def extract_views_and_reply_number(item_html):
        view_number = item_html.xpath('./div[@class="item-ft"]/p[@class="info"]/span[1]/em/text()')
        reply_number = item_html.xpath('./div[@class="item-ft"]/p[@class="info"]/span[2]/em/text()')
        return view_number[0], reply_number[0]
