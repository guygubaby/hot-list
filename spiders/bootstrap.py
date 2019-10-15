import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from concurrent.futures import ThreadPoolExecutor

from . import *

spider_list = [ZhihuSpider, HupuSpider, V2exSpider,WeiBoSpider]


def run_spider(Spider):
    spider = Spider()
    spider.run()


def run():
    with ThreadPoolExecutor(64) as executor:
        executor.map(run_spider, spider_list)


def init_scheduler():
    scheduler = BackgroundScheduler(timezone='UTC')
    scheduler.add_job(func=run, trigger='interval', minutes=30)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


def bootstrap():
    run()
    init_scheduler()
