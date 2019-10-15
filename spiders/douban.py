from utils.urls import douban_url
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class DoubanSpider(Spider):
    def __init__(self, name='douban'):
        super().__init__(name)

    def run(self):
        super().run()
        headers = HEADERS.copy()
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Referer'] = 'https://www.douban.com/group/explore'
        headers['Host'] = 'www.douban.com'
        res = requests.get(douban_url, headers=headers)
        res.encoding = 'utf-8'

        soup = BeautifulSoup(res.text, 'html.parser')

        _list = soup.select('div.channel-item')
        print(len(_list))
        for item in _list:
            a_el = item.select('div.bd a')[0]
            title = a_el.text.strip()
            url = a_el.get('href')

            desc = item.select('div.block p')[0].text.strip()

            hot_item = HotItem(title,url, cate=types['douban'],desc=desc)
            self.arr.append(hot_item)

        hot_collection.delete_many({'cate':types['douban']})
        hot_collection.insert_many([vars(item) for item in self.arr])
