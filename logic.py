# logic.py
class TicTacToeBoard:
    def __init__(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def make_move(self, movePositionX, movePositionY, playerFlag):
        if self.is_valid_move(movePositionX, movePositionY):
            if self.board[movePositionX][movePositionY] == '':
                if playerFlag:
                    self.board[movePositionX][movePositionY] = 'O'
                else:
                    self.board[movePositionX][movePositionY] = 'X'
                return True
        return False

    def is_valid_move(self, movePositionX, movePositionY):
        return 0 <= movePositionX < 3 and 0 <= movePositionY < 3

    def check_winner(self):
        for i in range(3):
            # Check horizontal
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '':
                return self.board[i][0]
            # Check vertical
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '':
                return self.board[0][i]

        # Check diagonal (top-left to bottom-right)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return self.board[0][0]

        # Check diagonal (top-right to bottom-left)
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return self.board[0][2]

        return None

    def is_draw(self):
        return all(self.board[i][j] for i in range(3) for j in range(3))
