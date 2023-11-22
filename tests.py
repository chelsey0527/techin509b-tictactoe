# tests.py
import unittest
from logic import make_empty_board, is_valid_move, make_move, check_winner, is_draw

class TicTacToeTests(unittest.TestCase):
    def test_make_empty_board(self):
        board = make_empty_board()
        self.assertTrue(all(all(cell == '' for cell in row) for row in board))

    def test_is_valid_move(self):
        self.assertTrue(is_valid_move(make_empty_board(), 0, 0))
        self.assertTrue(is_valid_move(make_empty_board(), 1, 1))
        self.assertTrue(is_valid_move(make_empty_board(), 2, 2))
        self.assertFalse(is_valid_move(make_empty_board(), -1, 0))
        self.assertFalse(is_valid_move(make_empty_board(), 3, 0))

    def test_make_move(self):
        board = make_empty_board()
        self.assertTrue(make_move(board, 0, 0, True))
        self.assertEqual(board, [['O', '', ''], ['', '', ''], ['', '', '']])
        self.assertTrue(make_move(board, 1, 1, False))
        self.assertEqual(board, [['O', '', ''], ['', 'X', ''], ['', '', '']])
        self.assertFalse(make_move(board, 0, 0, True))

    def test_check_winner(self):
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', 'O']]
        self.assertEqual(check_winner(board), 'X')

    def test_is_draw(self):
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', 'O']]
        self.assertTrue(is_draw(board))

    def test_immediate_win(self):
        board = [['X', 'O', 'X'],
                ['', 'O', ''],
                ['', '', '']]
        self.assertEqual(check_winner(board), 'O')

    def test_draw_on_last_move(self):
        board = [['X', 'O', 'X'],
                ['O', 'X', 'O'],
                ['O', 'X', '']]
        self.assertFalse(is_draw(board))


if __name__ == '__main__':
    unittest.main()
