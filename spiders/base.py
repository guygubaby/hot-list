class Spider:
    def __init__(self, name):
        # Thread.__init__(self)
        self.arr = []
        self.name = name

    def run(self):
        print("Starting {} ...".format(self.name))
