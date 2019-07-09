import gameboard
import view
import random
from pprint import pprint

random_row = random.randint(0,4)
random_column = random.randint(0,4)
ACTUAL_SHIP = (random_row, random_column)

guess_counter=0
max_guess = 25



board = gameboard.GameBoard()
board[random_row, random_column] = 'S'
#board[2,3]= 'X'
print(board)
repr(board)
# pprint(board[4,1])
# pprint(board.grid)


if board:
    print('Board was True!')
else:
    print('Board was False!')

while guess_counter < max_guess:
    (grid_row, grid_column) = view.get_coordinate_guess()
    if (grid_row, grid_column)==ACTUAL_SHIP:
        board[grid_row, grid_column]='H'
        print("You win")
    else:
        board[grid_row, grid_column]='M'

    #print(f"ROW: {grid_row} COLUMN: {grid_column}")
    print(board)
    guess_counter +=1
