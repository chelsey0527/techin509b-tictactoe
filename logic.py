# logic.py

def make_empty_board():
    return [['', '', ''], ['', '', ''], ['', '', '']]

def is_valid_move(board, movePositionX, movePositionY):
    return 0 <= movePositionX < 3 and 0 <= movePositionY < 3

def make_move(board, movePositionX, movePositionY, playerFlag):
    if board[movePositionX][movePositionY] == '':
        if playerFlag:
            board[movePositionX][movePositionY] = 'O'
        else:
            board[movePositionX][movePositionY] = 'X'
        return True
    else:
        return False

def check_winner(board):
    for i in range(3):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        # Check vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None

def is_draw(board):
    return all(board[i][j] for i in range(3) for j in range(3))
