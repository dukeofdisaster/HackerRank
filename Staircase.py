# STAIRCASE---
# Given an integer N, print a staircse of N steps high and N steps wide.
# Ex: Given N = 3
# output:   #
#          ##
#         ###



import sys

n = int(input())

def staircase():
    space = " "
    tempVal = n
    stairSize=1
    for i in range(n):
        print(space * ((tempVal)-1) + '#'*stairSize)
        stairSize += 1
        tempVal-= 1

staircase()

