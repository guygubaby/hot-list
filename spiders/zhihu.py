import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from utils.urls import ZHIHU_URL
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.time_used_wrapper import time_used
from utils.cates import types


class ZhihuSpider(Spider):
    def __init__(self, name='zhihu'):
        Spider.__init__(self, name)

    @time_used
    def run(self):
        super().run()
        res = requests.get(ZHIHU_URL,headers=HEADERS)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        top_list = soup.select('.row .box')
        for item in top_list:
            url = 'http://daily.zhihu.com/{}'.format(item.find('a').get('href'))
            title = item.select('span.title')[0].text
            hot_item = HotItem(title, url,cate=types['zhihu'])
            self.arr.append(hot_item)
        hot_collection.delete_many({'cate':types['zhihu']})
        hot_collection.insert_many([item.__dict__ for item in self.arr])

