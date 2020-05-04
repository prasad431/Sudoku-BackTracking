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
def valid(board, n, p):
    b_x = p[1] // 3
    b_y = p[0] // 3

    for i in range(b_y*3, b_y*3 + 3):
        for j in range(b_x*3, b_x*3 + 3):
            if board[i][j] == n and (i,j) != p:
                return False

    for i in range(len(board)):
        if board[i][p[1]] == n and p[0] != i:
            return False

    for i in range(len(board[0])):
        if board[p[0]][i] == n and p[1] != i:
            return False

    return True
