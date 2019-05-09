import battleship.game
import battleship.grid
import battleship.player
import battleship.ship

GAME_HEIGHT = 8
GAME_WIDTH = 8


def print_results(hits, ships_sunk, players_lost):
    print('Successful shots: (coordinate, player who was hit)')
    for shot, player in hits:
        print((shot.x, shot.y), id(player))
    for ship, player in ships_sunk:
        print('{}\'s {} was sunk at {}'.format(id(player), ship.__class__.__name__, list(ship.get_segments())))
    for player in players_lost:
        print('{} has lost'.format(id(player)))


def print_grid(grid):
    marks = grid.get_marks()
    for i in range(GAME_HEIGHT):
        for j in range(GAME_WIDTH):
            for mark in marks:
                if (mark.x, mark.y) == (i, j):
                    if isinstance(mark, battleship.grid.RedPeg):
                        print('X', end='')
                    elif isinstance(mark, battleship.grid.WhitePeg):
                        print('O', end='')
                    else:
                        print('-', end='')
                    break
            else:
                print('-', end='')
        print()


def main():
    p1 = battleship.player.Player(GAME_HEIGHT, GAME_WIDTH)
    p2 = battleship.player.Player(GAME_HEIGHT, GAME_WIDTH)
    p3 = battleship.player.Player(GAME_HEIGHT, GAME_WIDTH)
    players = [p1, p2, p3]

    # p2 and p3 placed their ships on the same tiles, but p2's ship is bigger
    p1.add_ship(battleship.ship.Cruiser    (0, 0, is_vertical=False))
    p2.add_ship(battleship.ship.Submarine  (1, 0, is_vertical=True ))
    p3.add_ship(battleship.ship.Destroyer  (1, 0, is_vertical=True ))

    g = battleship.game.Game(players, GAME_HEIGHT, GAME_WIDTH)

    s1 = battleship.game.Shot(p1, 1, 0) # Hit
    s2 = battleship.game.Shot(p2, 0, 0) # Hit
    s3 = battleship.game.Shot(p3, 3, 3) # Miss

    print()
    print('Round 1:')
    print()
    print_results(*g.process_shots([s1, s2, s3]))

    s1 = battleship.game.Shot(p1, 2, 2) # Miss
    s2 = battleship.game.Shot(p2, 0, 1) # Hit
    s3 = battleship.game.Shot(p3, 0, 2) # Hit

    print()
    print('Round 2:')
    print()
    print_results(*g.process_shots([s1, s2, s3]))

    s2 = battleship.game.Shot(p2, 2, 0) # Hit
    s3 = battleship.game.Shot(p3, 4, 4) # Miss

    print()
    print('Round 3:')
    print()
    print_results(*g.process_shots([s2, s3]))

    print()
    print('Final public grid:')
    print()

    print_grid(g.get_public_grid())

    print()
    print('Final private grid:')
    print()

    print_grid(g.get_private_grid())

    print()
    print('Final player grids:')
    print()

    print_grid(p1.get_grid())
    print()
    print_grid(p2.get_grid())
    print()
    print_grid(p3.get_grid())
    print()

if __name__ == '__main__':
    main()

    '''
    p1.add_ship(ship.Carrier    (0, 0, is_vertical=False))
    p1.add_ship(ship.Battleship (1, 0, is_vertical=True ))
    p1.add_ship(ship.Cruiser    (1, 1, is_vertical=False))
    p1.add_ship(ship.Submarine  (2, 3, is_vertical=False))
    p1.add_ship(ship.Destroyer  (3, 3, is_vertical=True ))
    '''
