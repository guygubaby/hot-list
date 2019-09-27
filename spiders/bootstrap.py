from . import *

thread_list = []

zhihu_spider = ZhihuSpider()
hupu_spider = HupuSpider()

thread_list.append(zhihu_spider)
thread_list.append(hupu_spider)


def bootstrap():
    for job in thread_list:
        job.start()
        job.join()
