from utils.urls import guokr_url
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class GuokrSpider(Spider):
    def __init__(self, name='guokr'):
        super().__init__(name)

    def run(self):
        super().run()
        headers = HEADERS.copy()
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Referer'] = 'https://www.guokr.com/scientific/'
        headers['Host'] = 'www.guokr.com'
        res = requests.get(guokr_url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        _list = soup.select('div.article')
        for item in _list:
            a_tag = item.find('a',class_='article-title')
            if a_tag:
                title = a_tag.text.strip()
                url = a_tag.get('href')
                desc = item.find('p',class_='article-summary').text.strip()
                hot_item = HotItem(title,url, cate = types['guokr'],desc = desc)
                self.arr.append(hot_item)
            else:
                continue
        hot_collection.delete_many({'cate':types['guokr']})
        hot_collection.insert_many([vars(item) for item in self.arr])



if __name__ == '__main__':
    s = GuokrSpider()
    s.run()
