


class Stack(object):
    def __init__(self, x=[]):
        self.list = x

    def stacking(self, new):
        self.list.insert(0, new)

    def offload(self):
        top = self.list.pop(0)
        return top

    def read(self):
        x = self.list[0]
        return x


class Queue(object):
    def __init__(self, x=[]):
        self.list = x

    def queueup(self, new):
        self.list = self.list.insert(len(self.list) - 1, new)

    def offload(self):
        nextup = self.list.pop(0)
        return nextup

    def read(self):
        x = self.list[0]
        return x
