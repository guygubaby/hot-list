import atexit
from multiprocessing import Pool
from apscheduler.schedulers.background import BackgroundScheduler

from . import *

thread_list = []

zhihu_spider = ZhihuSpider()
hupu_spider = HupuSpider()
v2ex_spider = V2exSpider()

thread_list.append(zhihu_spider)
thread_list.append(hupu_spider)
thread_list.append(v2ex_spider)


def run_spider():
    pool = Pool()
    for thread in thread_list:
        pool.apply_async(func=thread.run)
    pool.close()
    pool.join()


def init_scheduler():
    scheduler = BackgroundScheduler(timezone='UTC')
    scheduler.add_job(func=run_spider, trigger='interval', hours=1)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


def bootstrap():
    run_spider()
    init_scheduler()