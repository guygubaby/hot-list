from utils.time_used_wrapper import time_used

class Spider:
    def __init__(self, name):
        self.arr = []
        self.name = name

    @time_used
    def run(self):
        print("Starting {} ...".format(self.name))
