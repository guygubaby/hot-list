from utils.urls import V2EX_URL
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.time_used_wrapper import time_used
from utils.cates import types


class V2exSpider(Spider):
    def __init__(self, name='v2ex'):
        super().__init__(name)

    @time_used
    def run(self):
        super().run()
        res = requests.get(V2EX_URL,headers=HEADERS)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        _list = soup.select('.box a.topic-link')
        for item in _list:
            title = item.text
            url = 'https://www.v2ex.com{}'.format(item.get('href'))
            hot_item = HotItem(title, url, cate=types['v2ex'])
            self.arr.append(hot_item)

        hot_collection.delete_many({'cate':types['v2ex']})
        hot_collection.insert_many([item.__dict__ for item in self.arr])


