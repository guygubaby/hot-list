from utils.urls import baidu_url
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class BaiduSpider(Spider):
    def __init__(self, name='baidu'):
        super().__init__(name)

    def run(self):
        super().run()
        headers = HEADERS.copy()
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Host'] = 'top.baidu.com'
        res= requests.get(baidu_url,headers=HEADERS)
        res.encoding = 'gbk'

        soup = BeautifulSoup(res.text, 'html.parser')
        _list = soup.select('a.list-title')
        for item in _list:
            title = item.text.strip()
            url = item.get('href')
            hot_item = HotItem(title,url,cate=types['baidu'])

            self.arr.append(hot_item)

        hot_collection.delete_many({'cate':types['baidu']})
        hot_collection.insert_many([vars(item) for item in self.arr])



if __name__ == '__main__':
    s = BaiduSpider()
    s.run()