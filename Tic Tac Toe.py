# Building a tic tac toe game on my own in Python using OOP (Object Oriented Programming)

from random import choice
from time import sleep


class TicTacToe:
    pos_left = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self, board) -> None:
        self.board = board

    def replace_pos_with(self, pos_num):
        valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if pos_num in valid_nums:
            if pos_num in self.pos_left:
                self.board = str(self.board).replace(pos_num, 'X')
                self.pos_left = [w.replace(pos_num, 'X') for w in self.pos_left]
                return f"\n{str(self.board)}"
            else:
                return "The position you had choosed was already choosed. Please choose another spot."
        else:
            return "You have not entered a valid number. Please put a valid number again"

    def check_if_valid_input(self, input_num):
        valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if input_num not in valid_nums:
            return False
        else:
            return True

    def computer_play(self):
        computer_play_choice = ""
        while True:
            computer_play_choice = choice(pos_left)
            if computer_play_choice not in ['X', 'O']:
                break
        self.board = str(self.board).replace(computer_play_choice, 'O')
        self.pos_left = [w.replace(computer_play_choice, 'O') for w in self.pos_left]
        return f"\nI have guessed the number {computer_play_choice} \n{str(self.board)}"

    def check_if_any_winner(self):
        grid = self.pos_left

        # Complete checking for winner in sleeping line

        if grid[0] == 'X' and grid[1] == 'X' and grid[2] == 'X':
            return 1
        if grid[0] == 'O' and grid[1] == 'O' and grid[2] == 'O':
            return 0
        if grid[3] == 'X' and grid[4] == 'X' and grid[5] == 'X':
            return 1
        if grid[3] == 'O' and grid[4] == 'O' and grid[5] == 'O':
            return 0
        if grid[6] == 'X' and grid[7] == 'X' and grid[8] == 'X':
            return 1
        if grid[6] == 'O' and grid[7] == 'O' and grid[8] == 'O':
            return 0

        # Complete checking for winner in diagonal

        if grid[0] == 'X' and grid[4] == 'X' and grid[8] == 'X':
            return 1
        if grid[0] == 'O' and grid[4] == 'O' and grid[8] == 'O':
            return 0
        if grid[2] == 'X' and grid[4] == 'X' and grid[6] == 'X':
            return 1
        if grid[2] == 'O' and grid[4] == 'O' and grid[6] == 'O':
            return 0

        # Complete Checking for winner in standing line

        if grid[0] == 'X' and grid[3] == 'X' and grid[6] == 'X':
            return 1
        if grid[0] == 'O' and grid[3] == 'O' and grid[6] == 'O':
            return 0
        if grid[1] == 'X' and grid[4] == 'X' and grid[7] == 'X':
            return 1
        if grid[1] == 'O' and grid[4] == 'O' and grid[7] == 'O':
            return 0
        if grid[2] == 'X' and grid[5] == 'X' and grid[8] == 'X':
            return 1
        if grid[2] == 'O' and grid[5] == 'O' and grid[8] == 'O':
            return 0

        else:
            return False


player1 = input('Name of player: ')
board = "|1|2|3|\n|4|5|6|\n|7|8|9|\n"
game = TicTacToe(board=board)
print(f"""Hi, {player1}
Remember:
1. You are X, Computer is O
2. The numbers provided in the board is the positions, so please give in the correct position number based on the board.
""")
print(board)
game_is_on = True
while game_is_on:
    pos_num = input("Your spot: ")
    if pos_num in ["quit", 'Quit', 'QUIT']:
        break
    check_if_valid_input = game.check_if_valid_input(pos_num)
    result_after_pos_num = game.replace_pos_with(pos_num=pos_num)
    winner = game.check_if_any_winner()
    if winner != False:
        if winner == 1:
            print("The game has ended")
            print(f"The winner is {player1}")
            print('Here is the board:')
            print(game.board)
            break
        else:
            print("The game has ended")
            print(f"The winner is {player1}")
            print('Here is the board:')
            print(game.board)
            break
    pos_left = game.pos_left
    game_pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    check_if_pos_left = any(item in pos_left for item in game_pos)
    if check_if_pos_left == False:
        print("The game has ended")
        print("There is no winner in this game. It is a tie")
        print('Here is the board:')
        print(game.board)
        break
    if result_after_pos_num != "The position you had choosed was already choosed. Please choose another spot." and check_if_valid_input:
        print("Now, it is the computers turn. It is thinking")
        sleep(2)
        print(f"{game.computer_play()}")


