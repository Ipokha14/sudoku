

import time
board = [
[8, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 6, 0, 0, 0, 0, 0],
[0, 7, 0, 0, 9, 0, 2, 0, 0],
[0, 5, 0, 0, 0, 7, 0, 0, 0],
[0, 0, 0, 0, 4, 5, 7, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 3, 0],
[0, 0, 1, 0, 0, 0, 0, 6, 8],
[0, 0, 8, 5, 0, 0, 0, 1, 0],
[0, 9, 0, 0, 0, 0, 4, 0, 0]
]

def board_solver(bo):

    #choosing a place in the grid to make a guess
    empty_cell = find_empty(bo)

    row = empty_cell[0]
    col = empty_cell[1]

    #if there are no places left to guess, then puzzle is solved!
    if row is None:
        return True

    #if there is a place to guess, then make a guess between 1-9
    for num in range(1,10):
        #if the guess is valid, switch the empty value with the guessed nu,
        if valid(bo, num,(row,col)):
            bo[row][col] = num
            #recursively call the board solver function to guess remaining values
            #in the puzze
            if board_solver(bo):
                return True
        #if the recursion could not arrive at valid solution, then we start with
        # a new guess at initial position where we had started guessing
        bo[row][col] = 0

    #if nothing works at the end, return false, because puzzle is unsolvable
    return False



def find_empty(bo):
    #find a emptly place in the puzzle
    for i in range(len(bo)): # 1-9
        for j in range(len(bo[0])): #1-9
            if bo[i][j] == 0:
                return (i,j)
    #if no empty cells in puzzle, return tuple with None values
    return None, None



def valid(bo,num,pos):

    x_pos = pos[0]
    y_pos = pos[1]

    #checking rows to see if num exists
    row_vals = bo[x_pos]
    if num in row_vals:
        return False

    #checking rows to see if num exists
    col_vals = [bo[i][y_pos] for i in range(len(bo))]
    if num in col_vals:
        return False

    #checking rows to see if num exists in 3*3 grids
    x_grid = (x_pos // 3) * 3
    y_grid = (y_pos // 3) * 3

    for row in range(x_grid, x_grid + 3):
        for col in range(y_grid, y_grid + 3):
            if bo[row][col] == num:
                return False

    return True

def print_board(bo):
    length = len(bo)
    for i in range(length):
        if i % 3 == 0 and i != 0:
            print("===============================")
        for j in range(len(bo[0])):
            if  j % 3 == 0 and j!= 0:
                print(" | ", end = "") # don't print new line
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) , " ", end = "" ) #dont print newline


if __name__ == "__main__":
    print_board(board)
    print("***************************************")
    t1 = time.time()
    board_solver(board)
    t2 = time.time()
    print_board(board)
    print(f"Solved in {round((t2-t1), 3)} seconds! ")
