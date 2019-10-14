from utils.time_used_wrapper import time_used
import multiprocessing as mp


class Spider:
    def __init__(self, name):
        self.lock = mp.Lock()
        self.arr = []
        self.name = name

    @time_used
    def run(self):
        print("Starting {} ...".format(self.name))
