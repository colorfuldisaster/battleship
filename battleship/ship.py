class Ship(object):
    def __init__(self, x, y, is_vertical=False):
        if is_vertical:
            self.segments = {(x + i, y): False for i in range(self.SIZE)}
        else:
            self.segments = {(x, y + j): False for j in range(self.SIZE)}

    def get_segments(self):
        return self.segments

    def is_hit(self, x, y):
        return self.segments[(x, y)]

    def mark_hit(self, x, y):
        self.segments[(x, y)] = True

    def is_sunk(self):
        # True if all segments are mapped to True
        return all(self.segments.values())


class Carrier(Ship)     : SIZE = 5
class Battleship(Ship)  : SIZE = 4
class Cruiser(Ship)     : SIZE = 3
class Submarine(Ship)   : SIZE = 3
class Destroyer(Ship)   : SIZE = 2
