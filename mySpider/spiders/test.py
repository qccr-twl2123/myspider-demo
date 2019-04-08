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

start_urls = list()
with open(os.path.join(Path(__file__).parent, 'urls.txt'), 'r') as f:
    start_urls_list = f.readlines()
    for url in start_urls_list:
        start_urls.append(url)

print(start_urls)

list_demo = ['https://www.19lou.com/r/1/19lnsxq-39.html\n', 'https://www.19lou.com/r/1/19lnsxq-40.html\n',
             'https://www.19lou.com/r/1/19lnsxq-41.html\n', 'https://www.19lou.com/r/1/19lnsxq-42.html\n',
             'https://www.19lou.com/r/1/19lnsxq-43.html\n', 'https://www.19lou.com/r/1/19lnsxq-44.html\n',
             'https://www.19lou.com/r/1/19lnsxq-45.html\n', 'https://www.19lou.com/r/1/19lnsxq-46.html\n',
             'https://www.19lou.com/r/1/19lnsxq-47.html\n', 'https://www.19lou.com/r/1/19lnsxq-48.html\n',
             'https://www.19lou.com/r/1/19lnsxq-49.html\n', 'https://www.19lou.com/r/1/19lnsxq-50.html\n',
             'https://www.19lou.com/r/1/19lnsxq-51.html\n', 'https://www.19lou.com/r/1/19lnsxq-52.html\n',
             'https://www.19lou.com/r/1/19lnsxq-53.html\n', 'https://www.19lou.com/r/1/19lnsxq-54.html\n',
             'https://www.19lou.com/r/1/19lnsxq-55.html\n', 'https://www.19lou.com/r/1/19lnsxq-56.html\n',
             'https://www.19lou.com/r/1/19lnsxq-57.html\n', 'https://www.19lou.com/r/1/19lnsxq-58.html\n',
             'https://www.19lou.com/r/1/19lnsxq-59.html\n', 'https://www.19lou.com/r/1/19lnsxq-60.html\n',
             'https://www.19lou.com/r/1/19lnsxq-61.html\n', 'https://www.19lou.com/r/1/19lnsxq-62.html\n',
             'https://www.19lou.com/r/1/19lnsxq-63.html\n', 'https://www.19lou.com/r/1/19lnsxq-64.html\n',
             'https://www.19lou.com/r/1/19lnsxq-65.html\n', 'https://www.19lou.com/r/1/19lnsxq-66.html\n',
             'https://www.19lou.com/r/1/19lnsxq-67.html\n', 'https://www.19lou.com/r/1/19lnsxq-68.html\n',
             'https://www.19lou.com/r/1/19lnsxq-69.html\n', 'https://www.19lou.com/r/1/19lnsxq-70.html\n',
             'https://www.19lou.com/r/1/19lnsxq-71.html\n', 'https://www.19lou.com/r/1/19lnsxq-72.html\n',
             'https://www.19lou.com/r/1/19lnsxq-73.html\n', 'https://www.19lou.com/r/1/19lnsxq-74.html\n',
             'https://www.19lou.com/r/1/19lnsxq-75.html\n', 'https://www.19lou.com/r/1/19lnsxq-76.html\n',
             'https://www.19lou.com/r/1/19lnsxq-77.html\n', 'https://www.19lou.com/r/1/19lnsxq-78.html\n',
             'https://www.19lou.com/r/1/19lnsxq-79.html\n', 'https://www.19lou.com/r/1/19lnsxq-80.html\n',
             'https://www.19lou.com/r/1/19lnsxq-81.html\n', 'https://www.19lou.com/r/1/19lnsxq-82.html\n',
             'https://www.19lou.com/r/1/19lnsxq-83.html\n', 'https://www.19lou.com/r/1/19lnsxq-84.html\n',
             'https://www.19lou.com/r/1/19lnsxq-85.html\n', 'https://www.19lou.com/r/1/19lnsxq-86.html\n',
             'https://www.19lou.com/r/1/19lnsxq-87.html\n', 'https://www.19lou.com/r/1/19lnsxq-88.html\n',
             'https://www.19lou.com/r/1/19lnsxq-89.html\n', 'https://www.19lou.com/r/1/19lnsxq-90.html\n',
             'https://www.19lou.com/r/1/19lnsxq-91.html\n', 'https://www.19lou.com/r/1/19lnsxq-92.html\n',
             'https://www.19lou.com/r/1/19lnsxq-93.html\n', 'https://www.19lou.com/r/1/19lnsxq-94.html\n',
             'https://www.19lou.com/r/1/19lnsxq-95.html\n', 'https://www.19lou.com/r/1/19lnsxq-96.html\n',
             'https://www.19lou.com/r/1/19lnsxq-97.html\n', 'https://www.19lou.com/r/1/19lnsxq-98.html\n',
             'https://www.19lou.com/r/1/19lnsxq-99.html\n', 'https://www.19lou.com/r/1/19lnsxq-100.html\n',
             'https://www.19lou.com/r/1/19lnsxq-101.html\n', 'https://www.19lou.com/r/1/19lnsxq-102.html\n',
             'https://www.19lou.com/r/1/19lnsxq-103.html\n', 'https://www.19lou.com/r/1/19lnsxq-104.html\n',
             'https://www.19lou.com/r/1/19lnsxq-105.html\n', 'https://www.19lou.com/r/1/19lnsxq-106.html\n',
             'https://www.19lou.com/r/1/19lnsxq-107.html\n', 'https://www.19lou.com/r/1/19lnsxq-108.html\n',
             'https://www.19lou.com/r/1/19lnsxq-109.html\n', 'https://www.19lou.com/r/1/19lnsxq-110.html\n',
             'https://www.19lou.com/r/1/19lnsxq-111.html\n', 'https://www.19lou.com/r/1/19lnsxq-112.html\n',
             'https://www.19lou.com/r/1/19lnsxq-113.html\n', 'https://www.19lou.com/r/1/19lnsxq-114.html\n',
             'https://www.19lou.com/r/1/19lnsxq-115.html\n', 'https://www.19lou.com/r/1/19lnsxq-116.html\n',
             'https://www.19lou.com/r/1/19lnsxq-117.html\n', 'https://www.19lou.com/r/1/19lnsxq-118.html\n',
             'https://www.19lou.com/r/1/19lnsxq-119.html\n', 'https://www.19lou.com/r/1/19lnsxq-120.html\n',
             'https://www.19lou.com/r/1/19lnsxq-121.html\n', 'https://www.19lou.com/r/1/19lnsxq-122.html\n',
             'https://www.19lou.com/r/1/19lnsxq-123.html\n', 'https://www.19lou.com/r/1/19lnsxq-124.html\n',
             'https://www.19lou.com/r/1/19lnsxq-125.html\n', 'https://www.19lou.com/r/1/19lnsxq-126.html\n',
             'https://www.19lou.com/r/1/19lnsxq-127.html\n', 'https://www.19lou.com/r/1/19lnsxq-128.html\n',
             'https://www.19lou.com/r/1/19lnsxq-129.html\n', 'https://www.19lou.com/r/1/19lnsxq-130.html\n',
             'https://www.19lou.com/r/1/19lnsxq-131.html\n', 'https://www.19lou.com/r/1/19lnsxq-132.html\n',
             'https://www.19lou.com/r/1/19lnsxq-133.html\n', 'https://www.19lou.com/r/1/19lnsxq-134.html\n',
             'https://www.19lou.com/r/1/19lnsxq-135.html\n', 'https://www.19lou.com/r/1/19lnsxq-136.html\n',
             'https://www.19lou.com/r/1/19lnsxq-137.html\n', 'https://www.19lou.com/r/1/19lnsxq-138.html\n',
             'https://www.19lou.com/r/1/19lnsxq-139.html\n', 'https://www.19lou.com/r/1/19lnsxq-140.html\n',
             'https://www.19lou.com/r/1/19lnsxq-141.html\n', 'https://www.19lou.com/r/1/19lnsxq-142.html\n',
             'https://www.19lou.com/r/1/19lnsxq-143.html\n', 'https://www.19lou.com/r/1/19lnsxq-144.html\n',
             'https://www.19lou.com/r/1/19lnsxq-145.html\n', 'https://www.19lou.com/r/1/19lnsxq-146.html\n',
             'https://www.19lou.com/r/1/19lnsxq-147.html\n', 'https://www.19lou.com/r/1/19lnsxq-148.html\n',
             'https://www.19lou.com/r/1/19lnsxq-149.html\n', 'https://www.19lou.com/r/1/19lnsxq-150.html\n',
             'https://www.19lou.com/r/1/19lnsxq-151.html\n', 'https://www.19lou.com/r/1/19lnsxq-152.html\n',
             'https://www.19lou.com/r/1/19lnsxq-153.html\n', 'https://www.19lou.com/r/1/19lnsxq-154.html\n',
             'https://www.19lou.com/r/1/19lnsxq-155.html\n', 'https://www.19lou.com/r/1/19lnsxq-156.html\n',
             'https://www.19lou.com/r/1/19lnsxq-157.html\n', 'https://www.19lou.com/r/1/19lnsxq-158.html\n',
             'https://www.19lou.com/r/1/19lnsxq-159.html\n', 'https://www.19lou.com/r/1/19lnsxq-160.html\n',
             'https://www.19lou.com/r/1/19lnsxq-161.html\n', 'https://www.19lou.com/r/1/19lnsxq-162.html\n',
             'https://www.19lou.com/r/1/19lnsxq-163.html\n', 'https://www.19lou.com/r/1/19lnsxq-164.html\n',
             'https://www.19lou.com/r/1/19lnsxq-165.html\n', 'https://www.19lou.com/r/1/19lnsxq-166.html\n',
             'https://www.19lou.com/r/1/19lnsxq-167.html\n', 'https://www.19lou.com/r/1/19lnsxq-168.html\n',
             'https://www.19lou.com/r/1/19lnsxq-169.html\n', 'https://www.19lou.com/r/1/19lnsxq-170.html\n',
             'https://www.19lou.com/r/1/19lnsxq-171.html\n', 'https://www.19lou.com/r/1/19lnsxq-172.html\n',
             'https://www.19lou.com/r/1/19lnsxq-173.html\n', 'https://www.19lou.com/r/1/19lnsxq-174.html\n',
             'https://www.19lou.com/r/1/19lnsxq-175.html\n', 'https://www.19lou.com/r/1/19lnsxq-176.html\n',
             'https://www.19lou.com/r/1/19lnsxq-177.html\n', 'https://www.19lou.com/r/1/19lnsxq-178.html\n',
             'https://www.19lou.com/r/1/19lnsxq-179.html\n', 'https://www.19lou.com/r/1/19lnsxq-180.html\n',
             'https://www.19lou.com/r/1/19lnsxq-181.html\n', 'https://www.19lou.com/r/1/19lnsxq-182.html\n',
             'https://www.19lou.com/r/1/19lnsxq-183.html\n', 'https://www.19lou.com/r/1/19lnsxq-184.html\n',
             'https://www.19lou.com/r/1/19lnsxq-185.html\n', 'https://www.19lou.com/r/1/19lnsxq-186.html\n',
             'https://www.19lou.com/r/1/19lnsxq-187.html\n', 'https://www.19lou.com/r/1/19lnsxq-188.html\n',
             'https://www.19lou.com/r/1/19lnsxq-189.html\n', 'https://www.19lou.com/r/1/19lnsxq-190.html\n',
             'https://www.19lou.com/r/1/19lnsxq-191.html\n', 'https://www.19lou.com/r/1/19lnsxq-192.html\n',
             'https://www.19lou.com/r/1/19lnsxq-193.html\n', 'https://www.19lou.com/r/1/19lnsxq-194.html\n',
             'https://www.19lou.com/r/1/19lnsxq-195.html\n', 'https://www.19lou.com/r/1/19lnsxq-196.html\n',
             'https://www.19lou.com/r/1/19lnsxq-197.html\n', 'https://www.19lou.com/r/1/19lnsxq-198.html\n',
             'https://www.19lou.com/r/1/19lnsxq-199.html']


print([str(x).replace("\n", "") for x in list_demo])
