import time
import torch

gamefield = [
             1, 2, 3,
             4, 5, 6,
             7, 8, 9
            ]
WINCONS = [[1,2,3],
           [4,5,6],
           [7,8,9],
           [1,4,7],
           [1,5,9],
           [2,5,8],
           [3,6,9],
           [3,5,7]]
def findIfStanding(standing):
    standing == False
winnerFound = False
while winnerFound == True:
    xTurn = True
    print("=" * 15)
    print("Its x's turn. Write the index where you want to play")
    kerdes = int(input("Index here: "))