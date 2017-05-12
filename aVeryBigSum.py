# A Very Big Sum
# You're given an array of integers of size N. You need to print
# the sum of the elements in the array, keeping in mind some
# may be quite large'
#
#INPUT FORMAT
# The first line of the input consists of an integer N. The next
# line contains N space-separated integers contained in the array.A
#
#OUTPUT FORMAT
# Print a single value equal to the sum of the elements in the
# array.

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def arrSum(nums):


    total = 0
    for i in arr:
        total += i
    print(total)

arrSum(arr)