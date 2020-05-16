import numpy as np                               #importing numpy library
print(" Type entries in single line")

bo= np.array(list(map(int, input().split()))).reshape(5, 5)   # constructing 5x5 array from single line input

def validsolution(board):
    for i in range(len(board)):                  #length of board len(board)=5
        hadd=0                                   #horizontal addition variable
        vadd=0                                   #vertical addition variable
        for j in range(len(board)):
            vadd+=board[j][i]                    #adding vertical column
            hadd+=board[i][j]                    #adding horizontal column
            if board[i][j]<1 or board[i][j]>5:   #checking elements greater than 5 or less than 1
                return print(False)
        if vadd !=15 or hadd !=15:               #check if sum not equal to 15
            return print(False)
    return print(True)
validsolution(bo)
