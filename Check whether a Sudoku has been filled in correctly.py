import math
from random import seed, randint

# Returns whether the given Sudoku has been filled in correctly.
def is_valid_sudoku(sudoku):
    if len(sudoku) != len(sudoku[0]):
        return False


    n = len(sudoku)
    column = []
    is_valid = True
    for count in range(n): #Checking the different rows
        row = sudoku[count]
        for i in range(n):
            if i+1 not in row:
                is_valid = False
                break
            
    for i in range(n): #Checking the different columns
        column = []
        for count_1 in range(n):
            column.append(sudoku[count_1][i])
        for i in range(n):
            if i+1 not in column:
                is_valid = False
                break

    
    for mult in range(int(math.sqrt(n))): #Checking blocks
        for multiplier in range(int(math.sqrt(n))):
            square = []
            for k in range(int(math.sqrt(n))):
                for l in range(int(math.sqrt(n))):
                    square.append(sudoku[(int(math.sqrt(n)))*multiplier+k][(int(math.sqrt(n)))*mult+l])
            print(square)
            for i in range(n):
                if i+1 not in square:
                    is_valid = False
                    break


    return print(is_valid)
