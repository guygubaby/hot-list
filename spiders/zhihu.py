import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from utils.urls import ZHIHU_URL
from models.HotItem import HotItem
from utils.mongo import zhihu_db
from utils.time_used_wrapper import time_used


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
            hot_item = HotItem(title, url,category=self.name)
            self.arr.append(hot_item)
        zhihu_db.drop()
        for item in self.arr:
            zhihu_db.insert_one(item.__dict__)

