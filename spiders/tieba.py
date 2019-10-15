from utils.urls import tieba_url
import requests

from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class TiebaSpider(Spider):
    def __init__(self, name='tieba'):
        super().__init__(name)

    def run(self):
        super().run()
        res = requests.get(tieba_url,headers=HEADERS)
        res.encoding = 'utf-8'
        res = res.json()

        for item in res['data']['bang_topic']['topic_list']:
            hot_item = HotItem(title=item['topic_name'], url=item['topic_url'], cate=types['tieba'],desc=item['topic_desc'])
            self.arr.append(hot_item)

        hot_collection.delete_many({'cate':types['tieba']})
        hot_collection.insert_many([vars(item) for item in self.arr])

if __name__ == '__main__':
    s = TiebaSpider()
    s.run()