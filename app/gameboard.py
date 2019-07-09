BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'


class GameBoard:
    #initialize gameboard with all blanks
    def __init__(self, width=5, height=5):
        grid = []
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append(BLANK)
            grid.append(new_row)
        self.grid = grid

    #behind the scenes method to use indices
    def __getitem__(self,indices):
        col_index, row_index = indices #will unpack tuple
        return self.grid[row_index][col_index]

    def __setitem__(self, indices, value):
        print('Setting item at...', indices, "to", value)
        col_index, row_index = indices
        self.grid[row_index][col_index]=value
    #dunder string method
    #defined for every single class implicitly
    def __str__(self):
        #forward-facing user-friendly
        #how do you want this to look in our application
        #display everything except ships to user? #FIXME
        return('\n'.join(['\t|\t'.join([str(cell) for cell in row]) for row in self.grid]))

    def __bool__(self):
        for row in self.grid:
            for col in row:
                if col=='S':
                    return True
        return False

    
    def __repr__(self):
        #more for developer's benefit
        #show everything including ship
        return repr(self.grid)
        #return('\n'.join(['\t|\t'.join([str(cell) for cell in row]) for row in self.grid]))

    #get and set item methods




board = GameBoard()
board[2,3]= 'X'
print(board[4,1])
print(board.grid)

if board:
    print('Board was True!')
else:
    print('Board was False!')