#DIAGONAL DIFFERENCE
#
# Given a square matrix of size NxN, calculate the absolute difference between
# the sums of its diagonals
#
#INPUT FORMAT
# The first ling contains a single integer, N. The next N lines denote the
# matrix's rows, with each line containing N space-separated integers
# describing the columns.DIAGONAL
#
#CONSTRAINTS
# -100<= ELEMENTS IN MATRIX <= 100
#
#OUTPUT FORMAT
# Print the absoulute difference between the two sums of the matrix's diagonals
# as a single integer

#!/bin/python3

import sys
import math


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

def matriSum():
    total1 = 0
    total2 = 0
    finalSum = 0
    increment= n+1
    temp = 0
    temp2=0
    for i in range(len(a)):
        total1 = total1 + a[temp][temp]
        temp += 1
    for i in range (len(a)):
        total2 = total2 + a[temp2][(temp-1)-temp2]
        temp2 += 1
    #Uncomment the following 2 lines to
    #print(total1)
    #print(total2)e
    finalSum = abs(total1 - total2)

    print(finalSum)

matriSum()