class Ship(object):
    def __init__(self, x, y, is_vertical=False):
        if is_vertical:
            self._segments = {(x + i, y): False for i in range(self._SIZE)}
        else:
            self._segments = {(x, y + j): False for j in range(self._SIZE)}

    def get_segments(self):
        return list(self._segments)

    def is_at(self, x, y):
        return (x, y) in self._segments

    def mark_hit(self, x, y):
        self._segments[(x, y)] = True

    def is_sunk(self):
        # True if all segments are mapped to True
        return all(self._segments.values())


class Carrier(Ship)     : _SIZE = 5
class Battleship(Ship)  : _SIZE = 4
class Cruiser(Ship)     : _SIZE = 3
class Submarine(Ship)   : _SIZE = 3
class Destroyer(Ship)   : _SIZE = 2
