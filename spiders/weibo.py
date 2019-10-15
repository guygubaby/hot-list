from utils.urls import WEIBOT_URL
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class WeiBoSpider(Spider):
    def __init__(self, name='weibo'):
        super().__init__(name)

    def run(self):
        super().run()
        res = requests.get(WEIBOT_URL,headers=HEADERS)
        res.encoding = 'utf-8'

        soup = BeautifulSoup(res.text, 'html.parser')
        _list = soup.select('td.td-02 a')
        for item in _list:
            title = item.text.strip()
            url = 'https://s.weibo.com{}'.format(item.get('href'))
            hot_item = HotItem(title, url, cate=types['weibo'])
            self.arr.append(hot_item)
        hot_collection.delete_many({'cate':types['weibo']})
        hot_collection.insert_many([vars(item) for item in self.arr])
