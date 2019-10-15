from utils.urls import huxiu_url
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types

class HuxiuSpider(Spider):
    def __init__(self, name='huxiu'):
        super().__init__(name)

    def run(self):
        super().run()
        headers = HEADERS.copy()
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Referer'] = 'https://www.huxiu.com/channel/107.html'
        headers['Host'] = 'www.huxiu.com'
        res = requests.get(huxiu_url,headers=headers)
        res.encoding= 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        _list = soup.select('div.article-items')
        for item in _list:
            content_el = item.find('div',class_='article-item__content')
            a_tag = content_el.select('a')[-1]

            title = a_tag.find('h5',class_='article-item__content__title').text.strip()
            url = 'https://www.huxiu.com' + a_tag.get('href')
            desc = a_tag.find('p',class_='article-item__content__intro').text.strip()

            hot_item = HotItem(title,url, cate = types['huxiu'],desc=desc)
            self.arr.append(hot_item)
        hot_collection.delete_many({'cate':types['huxiu']})
        hot_collection.insert_many([vars(item) for item in self.arr])





if __name__ == '__main__':
    s = HuxiuSpider()
    s.run()