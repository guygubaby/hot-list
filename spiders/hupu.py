from utils.urls import HUPU_URL
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class HupuSpider(Spider):
    def __init__(self, name='hupu'):
        Spider.__init__(self, name)

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
            title = title.replace('zt','')
            hot_item = HotItem(title, url, cate=types['hupu'])
            self.arr.append(hot_item)
        hot_collection.delete_many({'cate':types['hupu']})
        hot_collection.insert_many([item.__dict__ for item in self.arr])
