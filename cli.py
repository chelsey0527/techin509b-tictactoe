# game.py
from logic import TicTacToeBoard
import random

class TicTacToeGame:
    def __init__(self, num_players, player_input):
        self.board = TicTacToeBoard()
        self.playerFlag = True  # True = O, False = X
        self.num_players = num_players
        self.player_input = player_input

    def display_board(self):
        self.board.display_board()

    def get_bot_move(self):
        # Generate random coordinates for the bot's move
        movePositionX = random.randint(0, 2)
        movePositionY = random.randint(0, 2)
        return movePositionX, movePositionY

    def play(self):
        while True:
            print("Current Game Board:")
            self.display_board()

            print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')

            if self.playerFlag or self.num_players == 2:  # Allow player input or for two players
                movePositionX, movePositionY = self.player_input()
            else:  # Bot's turn
                movePositionX, movePositionY = self.get_bot_move()
                print(f'Bot chooses X = {movePositionX}, Y = {movePositionY}')

            if self.board.is_valid_move(movePositionX, movePositionY):
                if self.board.make_move(movePositionX, movePositionY, self.playerFlag):
                    if self.playerFlag:
                        print("This is O's turn")
                    else:
                        print("This is X's turn")

                    winner = self.board.check_winner()
                    if winner:
                        print(winner, ' won')
                        break
                    elif self.board.is_draw():
                        print('Draw')
                        break

                    self.playerFlag = not self.playerFlag  # Switch player's turn
                else:
                    print(" ****** Invalid move. Try again. ****** ")
            else:
                print("Invalid position. X and Y must be between 0 and 2")

def user_input():
    movePositionX = int(input('Enter the X position you want to put: '))
    movePositionY = int(input('Enter the Y position you want to put: '))
    return movePositionX, movePositionY

if __name__ == '__main__':
    num_players = int(input("Enter the number of players (1 or 2): "))
    if num_players not in [1, 2]:
        print("Invalid number of players. Please choose 1 or 2.")
    else:
        game = TicTacToeGame(num_players, user_input)
        game.play()
