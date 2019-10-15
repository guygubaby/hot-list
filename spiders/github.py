from utils.urls import github_URL
import requests

from bs4 import BeautifulSoup
from spiders.base import Spider
from utils.headers import HEADERS
from models.HotItem import HotItem
from utils.mongo import hot_collection
from utils.cates import types


class GithubSpider(Spider):
    def __init__(self, name='github'):
        super().__init__(name)

    def run(self):
        super().run()
        res = requests.get(github_URL,headers=HEADERS)
        res.encoding = 'utf-8'

        soup = BeautifulSoup(res.text, 'html.parser')
        repository = soup.select('article.Box-row')

        for row in repository:
            title = row.select('h1.h3.lh-condensed')[0].text.strip()
            title = title.replace(' ','').replace('\n','')
            url = 'https://github.com' + row.select('h1.h3.lh-condensed')[0].find('a').get('href')
            desc_el = row.select('p.col-9')
            desc = desc_el[0].text.strip() if desc_el else None
            hot_item = HotItem(title, url, cate=types['github'], desc=desc)
            self.arr.append(hot_item)

        hot_collection.delete_many({'cate':types['github']})
        hot_collection.insert_many([vars(item) for item in self.arr])
