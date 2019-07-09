print('Welcome.  This is as simple game based on the classic board game Battleship')


def get_coordinate_guess():
    VALID_INPUT = False
    #to make this more intuitive for user accept number 1, 2, 3, 4, or 5 
    #rather than number between 0 and 4
    while VALID_INPUT == False:
        try:
            coordinate_guess_column = int(input("Enter number between 1 and 5 for column:")) 
            if coordinate_guess_column not in [1,2,3,4,5]:
                raise Exception
            coordinate_guess_row = int(input("Enter number between 1 and 5 for row:"))
            if coordinate_guess_row not in [1,2,3,4,5]:
                raise Exception
        except:
            print("Invalid input.  Try again")
        else:
            VALID_INPUT = True
            print(f"You guessed: row {coordinate_guess_row}, column {coordinate_guess_column}")
            coordinate_guess_row-=1
            coordinate_guess_column-=1
    return coordinate_guess_column, coordinate_guess_row
