import battleship.grid as grid
import battleship.ship as ship

class Player(object):
    def __init__(self, height, width, ships=None):
        self._grid = grid.Grid(height, width)
        if ships is None:
            self._ships = []
        else:
            self._ships = ships

    def can_add_ship(self, ship):
        existing_segments = sum([elem.get_segments() for elem in self._ships], [])
        # Check if any ship segment (x, y) already exists for this player
        return not any([segment in existing_segments for segment in ship.get_segments()])

    def add_ship(self, ship):
        self._ships.append(ship)

    def has_ship_at(self, x, y):
        # Check if any ship exists at (x, y)
        return any([ship.is_at(x, y) for ship in self._ships])

    def mark_hit(self, x, y):
        for ship in self._ships:
            if ship.is_at(x, y):
                ship.mark_hit(x, y)

    def get_sunk_ships(self):
        return [ship for ship in self._ships if ship.is_sunk()]

    def has_ships_remaining(self):
        # Check if the list of sunk ships does not equal the overall list of ships
        return not set(self.get_sunk_ships()) == set(self._ships)
