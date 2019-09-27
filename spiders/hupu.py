from utils.urls import HUPU_URL
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hupu_db
from utils.time_used_wrapper import time_used


class HupuSpider(Spider):
    def __init__(self, name='hupu'):
        Spider.__init__(self, name)

    @time_used
    def run(self):
        super().run()
        res = requests.get(HUPU_URL,headers=HEADERS)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        top_list = soup.select('.bbsHotPit li')
        for item in top_list:
            a_tag = item.select('.textSpan a')[0]
            url = 'https://bbs.hupu.com/{}'.format(a_tag.get('href'))
            title = a_tag.get('title')
            hot_item = HotItem(title, url, category=self.name)
            self.arr.append(hot_item)
        hupu_db.drop()
        for item in self.arr:
            hupu_db.insert_one(item.__dict__)
