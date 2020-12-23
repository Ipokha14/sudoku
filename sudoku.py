

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


    empty_cell = find_empty(bo)
    if not empty_cell:
        return True
    else:
        row = empty_cell[0]
        col = empty_cell[1]

    for num in range(1,10):
        if valid(bo, num,(row,col)):
            bo[row][col] = num
            bool_ = board_solver(bo)
            if bool_:
                return True

            bo[row][col] = 0
    return False



def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None



def valid(bo,num,pos):
    #checking rows to see if num exists
    x_pos = pos[0]
    y_pos = pos[1]

    for i in range(0,len(bo)):
        if bo[x_pos][i] == num and y_pos != i:
            return False

    #checking columns to see if num exists
    for i in range(0,len(bo)):
        if bo[i][y_pos] == num and x_pos != i:
            return False
    #check 3*3 boxes to see if the number exists

    box_x = (y_pos // 3)
    box_y = (x_pos // 3)

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x *3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True
#
def print_board(bo):
    length = len(bo)
    for i in range(length):
        if i % 3 == 0 and i != 0:
            print("===============================")
        for j in range(len(bo[0])):
            if  j % 3 == 0 and j!= 0:
                print(" | ", end = "")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) , " ", end = "" )


if __name__ == "__main__":

    print_board(board)
    print("***************************************")
    t1 = time.time()
    board_solver(board)
    t2 = time.time()
    print_board(board)
    print(f"Solved in {round((t2-t1), 3)} seconds! ")


# print("Unsolved")
# print_board(board)
# t1 = time.time()
# board_solver(board)
# print("Solved")
# t2 = time.time()
# print_board(board)
# print(f"Solved in {round((t2-t1),3)} seconds!")
