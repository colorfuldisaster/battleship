import collections


Peg = collections.namedtuple("Peg", ["x", "y"])

class RedPeg(Peg): pass
class WhitePeg(Peg): pass


class Grid(object):
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._marks = []

    def mark(self, peg):
        self._marks.append(peg)

    def get_marks(self):
        return self._marks

    def clear(self):
        self._marks = []

