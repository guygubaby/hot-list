from utils.urls import tinaya_url
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class TianyaSpider(Spider):
    def __init__(self, name='tianya'):
        super().__init__(name)

    def run(self):
        super().run()
        headers = HEADERS.copy()
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Referer'] = 'http://bbs.tianya.cn/list.jsp?item=funinfo&grade=3&order=1'
        headers['Host'] = 'bbs.tianya.cn'
        res = requests.get(tinaya_url,headers=HEADERS)

        soup = BeautifulSoup(res.text, 'html.parser')

        _list = soup.select('td.td-title')

        for item in _list:
            a_tag = item.find('a')
            title = a_tag.text.strip()
            url = 'http://bbs.tianya.cn' + a_tag.get('href')

            hot_item = HotItem(title,url,cate = types['tianya'])
            self.arr.append(hot_item)

        hot_collection.delete_many({'cate':types['tianya']})
        hot_collection.insert_many([vars(item) for item in self.arr])


if __name__ == '__main__':
    s = TianyaSpider()
    s.run()