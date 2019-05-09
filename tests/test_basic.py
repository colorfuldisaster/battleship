import battleship.grid as grid
import battleship.ship as ship

import unittest

CRUISER_SIZE = 3
CRUISER_X = 2
CRUISER_Y = 5

GRID_HEIGHT = 3
GRID_WIDTH = 4


class ShipTest(unittest.TestCase):

    def test_horizontal_segments(self):
        s = ship.Cruiser(CRUISER_X, CRUISER_Y)

        segments = s.get_segments()
        for j in range(CRUISER_SIZE):
            self.assertTrue((CRUISER_X, CRUISER_Y + j) in segments)
            self.assertTrue(s.is_at(CRUISER_X, CRUISER_Y + j))

    def test_vertical_segments(self):
        s = ship.Cruiser(CRUISER_X, CRUISER_Y, is_vertical=True)

        segments = s.get_segments()
        for i in range(CRUISER_SIZE):
            self.assertTrue((CRUISER_X + i, CRUISER_Y) in segments)
            self.assertTrue(s.is_at(CRUISER_X + i, CRUISER_Y))

    def test_sinking(self):
        s = ship.Cruiser(CRUISER_X, CRUISER_Y)
        self.assertFalse(s.is_sunk())

        for j in range(CRUISER_SIZE):
            s.mark_hit(CRUISER_X, CRUISER_Y + j)
        self.assertTrue(s.is_sunk())


class GridTest(unittest.TestCase):

    def test_marking(self):
        g = grid.Grid(GRID_HEIGHT, GRID_WIDTH)

        # Receive no marks
        self.assertTrue(set(g.get_marks()) == set())

        marks = [grid.WhitePeg(1, 1), grid.RedPeg(2, 3), grid.RedPeg(2, 4)]
        for mark in marks:
            g.mark(mark)

        # Receive the set of pegs that were marked
        self.assertTrue(set(g.get_marks()) == set(marks))

    def test_mark_clearing(self):
        g = grid.Grid(GRID_HEIGHT, GRID_WIDTH)
        self.assertTrue(set(g.get_marks()) == set())

        marks = [grid.WhitePeg(1, 1), grid.RedPeg(2, 3), grid.RedPeg(2, 4)]
        for mark in marks:
            g.mark(mark)

        # Clear all marks
        g.clear()
        self.assertTrue(set(g.get_marks()) == set())

        # Clear despite having no marks
        g.clear()
        self.assertTrue(set(g.get_marks()) == set())
