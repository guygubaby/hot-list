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
        headers = HEADERS.copy()
        headers.update(
            referer='https://www.zhihu.com/signin?next=%2Fhot',
            cookie='tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; _zap=4369dfa8-8757-4a0a-9b23-114fe13b449c; _xsrf=8ce5a6f2-6d38-4c4f-8a94-f343511a4dc8; d_c0="AMDmP0jPHRCPTnmL4dcBXTUEm7lWNYvWtO0=|1569658401"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569658400; capsion_ticket="2|1:0|10:1569658401|14:capsion_ticket|44:YThjZTVmZmI3NDQwNGRlNGIyZTQ5NmQzYzUzZTY0MGQ=|62c39d95c612658919bf053eb0b13b70ccddcde4d6b4c534127f37c900e2411e"; l_n_c=1; r_cap_id="NTkxYTFkN2M3ODZiNDJmNTlkYTVhNzBiZjEzODIxYTA=|1569658760|3f15e311b6f99af3f1d95ed3a1ea1619ac75eef1"; cap_id="M2E1OWVmNTM5YjMwNDQ4M2JkZGIyN2IyYmUxYWYwYzA=|1569658760|be545d54fcaeacdd6084952d60d42c2a6477e9dc"; l_cap_id="OTg5NTkzMGEzZDcxNGU0ZDhjZmYyYWI0MzZjOWFmYTE=|1569658760|e4477741cdddda2bf782bbefac43bdb6dc414112"; n_c=1; z_c0=Mi4xejFiZEFRQUFBQUFBd09ZX1NNOGRFQmNBQUFCaEFsVk5rbVY4WGdBdS04a1NoY0otV0ZUQk5ydjh0a0RGb2ZjaFBn|1569658770|1b7f9d825f104d60dc719882276ec00880677c27; tshl=; tst=h; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569659055; unlock_ticket="ABDMJM49ZggXAAAAYQJVTbkfj12-gPv33gH7u9Oq7-u4wMqZ5VMUMw=="'
        )
        res = requests.get(ZHIHU_URL,headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        top_list = soup.select('.HotList-list .HotItem-content')
        for item in top_list:
            a_tag = item.find('a')
            url = a_tag.get('href')
            title = a_tag.get('title')
            desc_tag = item.select('p')
            desc = desc_tag[0].text if desc_tag else None
            hot_item = HotItem(title, url,cate=types['zhihu'],desc=desc)
            self.arr.append(hot_item)
        hot_collection.delete_many({'cate':types['zhihu']})
        hot_collection.insert_many([item.__dict__ for item in self.arr])

