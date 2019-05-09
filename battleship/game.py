import battleship.grid as grid

import collections


Shot = collections.namedtuple("Shot", ['player', 'x', 'y'])


class Game(object):
    def __init__(self, players, grid_height, grid_width, is_stealth_mode=True):
        self._players = players
        self._public_grid = grid.Grid(grid_height, grid_width)
        self._is_stealth_mode = is_stealth_mode

    def process_shots(self, shots):
        successful_shots = []
        ships_sunk_before = sum([player.get_sunk_ships() for player in self._players], [])
        players_lost_before = [player for player in self._players if player.has_ships_remaining()]

        for shot in shots:
            for player in self._players:
                if player.has_ship_at(shot.x, shot.y):
                    player.mark_shit_hit(shot.x, shot.y)
                    # Add to list of successful shots, to be announced later
                    successful_shots.append((shot, player))

            # Was any player's ship hit?
            if any([player.has_ship_at(shot.x, shot.y) for player in self._players]):
                # Mark the "hit" on all player grids and the public grid
                for elem in self._players:
                    elem.get_grid().mark(grid.RedPeg(shot.x, shot.y))
                self._public_grid.mark(grid.RedPeg(shot.x, shot.y))

            # If not, the shot was a "miss"
            else:
                if self._is_stealth_mode:
                    # If stealth mode, only mark the "miss" on the shooting player's board
                    shot.player.get_grid().mark(grid.WhitePeg(shot.x, shot.y))
                else:
                    # Mark the "miss" publicly
                    self._public_grid.mark(grid.WhitePeg(shot.x, shot.y))

        ships_sunk_after = sum([player.get_sunk_ships() for player in self._players], [])
        ships_sunk = set(ships_sunk_after) - set(ships_sunk_before)

        players_lost_after = [player for player in self._players if player.has_ships_remaining()]
        players_lost = set(players_lost_after) - set(players_lost_before)

        return successful_shots, ships_sunk, players_lost
