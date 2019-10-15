from utils.urls import qdaily_url
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types

class QdailySpider(Spider):
    def __init__(self, name='qdaily'):
        super().__init__(name)

    def run(self):
        super().run()
        headers = HEADERS.copy()
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Referer'] = 'https://www.qdaily.com/tags/30.html'
        headers['Host'] = 'www.qdaily.com'
        res = requests.get(qdaily_url,headers=headers)
        res.encoding= 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        _list = soup.select('div.packery-item.article')
        for item in _list:
            title_tag = item.find('h3',class_='title')
            if title_tag:
                title = title_tag.text.strip()
                url = 'https://qdaily.com' + item.find('a',class_='com-grid-banner-article').get('href')
            else:
                a_tag = item.find('a',class_='com-grid-article')
                url = 'https://qdaily.com' + a_tag.get('href')
                title = a_tag.find('h3',class_='smart-dotdotdot').text.strip()
            hot_item = HotItem(title, url, cate=types['qdaily'])
            self.arr.append(hot_item)
        hot_collection.delete_many({'cate':types['qdaily']})
        hot_collection.insert_many([vars(item) for item in self.arr])

