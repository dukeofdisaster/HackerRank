#---MINI-MAX SUM
# Given 5 positive integers, find the minimum and maximum values that can be
# calculated by summing exactly 4 of the five integers. Then print the
# respective minimum and maximum values as a single lien of two space-separated
# long integers.

import sys

a,b,c,d,e = raw_input().split(' ')
a,b,c,d,e = [int(a), int(b), int(c), int(d), int(e)]

def miniMaxSum():
    min = a
    max = a
    maxSum = 0
    minSum = 0

    # Since the input values are taken as a tuple (a, b, c, d, e) we can iterate
    # over them using the special for loop below; i is the index, x is the value

    for i,x in enumerate([a, b, c, d, e]):
        if x <= min:
            min = x
        if x >= max:
            max = x

    maxSum = (a+b+c+d+e) - min
    minSum = (a+b+c+d+e) - max
    print(minSum, maxSum)

miniMaxSum()