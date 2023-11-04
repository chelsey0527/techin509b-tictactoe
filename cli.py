# cli.py
from logic import make_empty_board, is_valid_move, make_move, check_winner, is_draw

def display_board(board):
    for row in board:
        print(' '.join(row))

def main():
    while True:
        board = make_empty_board()
        playerFlag = True  # True = O, False = X

        while True:
            print("Current Game Board:")
            display_board(board)

            print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
            movePositionX = int(input('Enter the X position you want to put: '))
            movePositionY = int(input('Enter the Y position you want to put: '))

            if is_valid_move(board, movePositionX, movePositionY):
                if make_move(board, movePositionX, movePositionY, playerFlag):
                    if playerFlag:
                        print("This is O's turn")
                    else:
                        print("This is X's turn")

                    winner = check_winner(board)
                    if winner:
                        print(winner, ' won')
                        break
                    elif is_draw(board):
                        print('Draw')
                        break

                    playerFlag = not playerFlag  # Switch player's turn
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid position. X and Y must be between 0 and 2.")

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == '__main__':
    main()
