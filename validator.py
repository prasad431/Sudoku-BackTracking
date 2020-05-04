##
#This module is for vaidating the numbers of each box
##

#Inorder to find empty box in board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

#validate the box, coloumn, row
def valid(board, num, pos):
    b_x = pos[1] // 3
    b_y = pos[0] // 3

    for i in range(b_y*3, b_y*3 + 3):
        for j in range(b_x * 3, b_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    return True
