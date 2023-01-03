#!/usr/bin/env python3
# Tassin Ongsakul(dossdy)
# 640510615
# Lab11_2
# 204111 Sec 001

def main():
    board = [[7, 12, 1, 14],
 [2, 13, 8, 11],
 [16, 3, 10, 5],
 [9, 6, 15, 4]]
    print (is_magic_square(board))




def is_magic_square(board):
    v = []
    d = []
    for i in range(len(board)):
        if board[i] not in v:
            v.append(board[i])
        else: 
            d.append(board[i])
    if len(d)>0:
        return False
    # check size
    for i in range(len(board)):
       if len(board[i]) != len(board):
          return False
          
    # check row sums
    for r in board:
       if sum(r) != sum(board[0]):
          return False
    
    # check column sums
    cols = [[r[c] for r in board] for c in range(len(board[0]))]
    for c in cols:
       if sum(c) != sum(board[0]):
          return False
       
    return True
if __name__ == '__main__':
    main()
