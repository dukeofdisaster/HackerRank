#--BIRTHDAY CAKE CANDLES---
# Colleen is turning n years old; she has N candles of various heights. Candle
# i has height_i. Becuase the taller candles tower over the shorter ones, she
# can only blow out the tallest candles. Given the height_i for each individual
# candle, find and print the number of candles she can blow out.
#
# INPUT FORMAT--
# First line has a single integer, N, denoting number of candles. Second line
# contains N, space-separated integers, where each integer I describes the
# height of candle i.
#
# OUTPUT FORMAT--
# Print the number of candles colleen blows out on a new line
#
# Note: To me it looks like the easiest way to complete the task is to iterate
# through the height list once to extract the max value, then iterate through it
# again comparing the values to the max: if a value is equal to the max, we
# increment a counter, then print the counter total.
###############################################################################
# NOTE: In hacker rank the input code actually looks different, hackerrank
#        actually calls .strip().split(' ') on the input, but when we try and
#        run this code outside of the hackerrank site the compiler throws an
#        error stating "int has no attribute 'split'". You can remove the call
#        to the split function and still have the same functionality in the
#        program
###############################################################################


import sys
n = int(input())
height = [int(height_temp) for height_temp in raw_input().strip().split(' ')]

def getCandles():
    maxCandle = 0
    count = 0
    for x in height:
        if maxCandle < x:
            maxCandle = x
    print(maxCandle)

    for x in height:
        if x == maxCandle:
            count += 1
    print(count)

getCandles()