import battleship.grid as grid

import collections


Shot = collections.namedtuple("Shot", ['player', 'x', 'y'])


class Game(object):
    def __init__(self, players, grid_height, grid_width):
        self._players = players
        self._public_grid = grid.Grid(grid_height, grid_width)
        self._private_grid = grid.Grid(grid_height, grid_width)

    def get_public_grid(self):
        return self._public_grid

    def get_private_grid(self):
        return self._private_grid

    def process_shots(self, shots):
        successful_shots = []
        ships_sunk = set()
        players_lost = set()

        alive_players = [player for player in self._players if player.has_ships_remaining()]

        for shot in shots:
            for player in alive_players:
                if player.has_ship_at(shot.x, shot.y):
                    ships_sunk_before = set(player.get_sunk_ships())
                    player.mark_ship_hit(shot.x, shot.y)
                    ships_sunk_delta = set(player.get_sunk_ships()) - ships_sunk_before

                    # Update results: hits, sinks, losers
                    successful_shots.append((shot, player)) # (hit, player which got hit)
                    for ship in ships_sunk_delta:
                        ships_sunk.add((ship, player))      # (ship, ship's owner)
                    if not player.has_ships_remaining():
                        players_lost.add(player)

            # Was any player's ship hit?
            if any([player.has_ship_at(shot.x, shot.y) for player in self._players]):
                # Mark the "hit" on all player grids
                for elem in self._players:
                    elem.get_grid().mark(grid.RedPeg(shot.x, shot.y))
                # And on the global grids
                self._public_grid.mark(grid.RedPeg(shot.x, shot.y))
                self._private_grid.mark(grid.RedPeg(shot.x, shot.y))

            # If not, the shot was a "miss"
            else:
                # Only mark the "miss" on the shooting player's grid
                shot.player.get_grid().mark(grid.WhitePeg(shot.x, shot.y))
                # And on the global private grid
                self._private_grid.mark(grid.WhitePeg(shot.x, shot.y))

        return successful_shots, ships_sunk, players_lost
