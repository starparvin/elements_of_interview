import random
import math
def soduko_is_valid(sudoku):
    print(len(sudoku))

    for row in sudoku:
        checker = [False] * (len(sudoku) + 1)
        for column in row:
            if column != 0 and checker[column]:
                return False
            else:
                checker[column] = True

    for i in range(len(sudoku)):
        checker = [False] * (len(sudoku) + 1)
        for j in range(len(sudoku)):
            if sudoku[j][i] != 0 and checker[sudoku[j][i]]:
                return False
            else:
                checker[sudoku[j][i]] = True
    range_size = int(math.sqrt(len(sudoku)))
    for i in range(range_size):
        for j in range(range_size):
            checker = [False] * (len(sudoku) + 1)
            for i_i in range(range_size):
                for j_j in range(range_size):
                    number = sudoku[range_size*i+i_i][range_size*j+j_j]
                    if number !=0 and checker[number]:
                        return False
                    else:
                        checker[number] = True
    return True



def random_fill(sudoku):
    for row in sudoku:
        for i in range(len(row)):
            row[i] = random.randint(1,9)
def print_sudoku(sudoku):
    for row in sudoku:
        print(row)


sudoku = [[0]*9 for i in range(9)]
print(sudoku)
#random_fill(sudoku)
sudoku[0][0] = 1
sudoku[1][3] = 1
sudoku[2][6] = 1
sudoku[3][1] = 1
sudoku[4][4] = 1
sudoku[5][7] = 1
sudoku[6][2] = 1
sudoku[7][5] = 1
sudoku[8][8] = 1
print_sudoku(sudoku)
print(soduko_is_valid(sudoku))