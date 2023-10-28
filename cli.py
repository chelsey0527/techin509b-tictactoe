# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

# Import necessary libraries
# from logic import make_empty_board

# Function: winner checker
def TicTacToe(board):
    winner = ''
    winnerCount = 0

    # Add edge case
    if board == []:
      print('No board input!')
      return

    if len(board) != len(board[0]):
      print('Wrong board format!')
      return

    # Check diagonal (topleft to bottomright)
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        winnerCount += 1

    # Check diagonal (topright to bottomleft)
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        winnerCount += 1

    # Check horizontal and vertical
    for i in range(len(board)):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2]:
            winner = board[i][0]
            winnerCount += 1

        # Check vertical
        if board[0][i] == board[1][i] == board[2][i]:
            winner = board[0][i]
            winnerCount += 1

    if winnerCount == 1:
        print(winner, ' won')
    elif winnerCount == 0:
        print('Draw')

    return winner

# Main function
if __name__ == '__main__':
    while True:  # Keep playing until there's a winner or a draw
        # board = make_empty_board()
        board = [['', '', ''], ['', '', ''], ['', '', '']]
        playerFlag = True  # True = O, False = X

        while True:  # Keep taking turns until there's a winner or a draw
            print("TODO: take a turn!")

            # TODO: Show the board to the user.
            print('Game board:')
            for row in board:
                print(' '.join(row))

            # TODO: Input a move from the player.
            movePositionX = int(input('Enter the X position you want to put: '))
            movePositionY = int(input('Enter the Y position you want to put: '))

            # TODO: Update the board.
            if board[movePositionX][movePositionY] == '':
                if playerFlag:
                    board[movePositionX][movePositionY] = 'O'
                else:
                    board[movePositionX][movePositionY] = 'X'
            else:
                print("Invalid move. Try again.")
                continue

            # TODO: Update who's turn it is.
            if playerFlag:
                print("This is O's turn")
                playerFlag = False
            else:
                print("This is X's turn")
                playerFlag = True

            # Check for a winner
            winner = TicTacToe(board)
            if winner:
                break

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
