import collections


Peg = collections.namedtuple("Peg", ["x", "y"])

class RedPeg(Peg): pass
class WhitePeg(Peg): pass


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.marks = []

    def mark(self, peg):
        self.marks.append(peg)

    def get_marks(self):
        return self.marks

    def clear(self):
        self.marks = []

