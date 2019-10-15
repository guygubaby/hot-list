from utils.urls import url_36kr
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types

class Spider36kr(Spider):
    def __init__(self, name='36kr'):
        super().__init__(name)


    def run(self):
        super().run()
        headers = HEADERS.copy()
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Referer'] = 'https://36kr.com/'
        headers['Host'] = '36kr.com'
        res = requests.get(url_36kr,headers=HEADERS)
        res.encoding = 'utf-8'

        soup = BeautifulSoup(res.text, 'html.parser')
        _list = soup.select('div.kr-home-flow-item')
        for item in _list:
            a_tag = item.select('a.article-item-title')
            if a_tag:
                title = a_tag[0].text.strip()
                url = 'https://36kr.com' + a_tag[0].get('href')
                desc = item.select('a.article-item-description')[0].text.strip()

                hot_item = HotItem(title,url, cate = types['36kr'],desc = desc)
                self.arr.append(hot_item)
            else:
                continue
        hot_collection.delete_many({'cate':types['36kr']})
        hot_collection.insert_many([vars(item) for item in self.arr])



if __name__ == '__main__':
    s = Spider36kr()
    s.run()