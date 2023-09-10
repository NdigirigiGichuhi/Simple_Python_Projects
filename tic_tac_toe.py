#!/usr/bin/python3

#Creating the board dictionary
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#printing the board
def printBoard(board):
    print("{}|{}|{}".format(board['top-L'], board['top-M'], board['top-R']))
    print("{}{}{}{}{}".format('-','+', '-', '+', '-'))
    print("{}|{}|{}".format(board['mid-L'], board['mid-M'], board['mid-M']))
    print("{}{}{}{}{}".format("-", "+", "-", "+", "-"))
    print("{}|{}|{}".format(board['low-L'], board['low-M'], board['low-R']))

turn = 'X'
for i in range(9):
    printBoard(theBoard)

    print("Turn for {}. Move on which space?".format(turn))
    move = input()
    theBoard[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print(theBoard)

