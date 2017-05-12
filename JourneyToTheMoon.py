###############################################################################
# JOURNEY TO THE MOON--
#
# The UN is planning to send 2 people to the moon, from 2 different countries.
# There are N trained astronauts numbered from 0 to N-1. but those in charge of
# the mission did not receive information about the citizenship of each
# astronaut.The only information they have is that some particular pairs belong
# to the same country.
#
# Compute in how many ways they can pick a pair of astronauts belonging to
# different countries. Assume that you are provided enough pairs to let you
# identify the groups of astronauts even though you might not know their
# country directly. For instance, if 1,2,3 are astronauts from the same country
# it is sufficient to mention that (1,2) and (2,3) are paris of astronauts from
# the same country without providing information about a third pair (1,3).
#
# INPUT FORMAT
#
# The first line contains two integers, N and P, separated by a single space. P
# lines follow. Each line contains 2 integers separated by a single space A and
# B such that 0 <= A,B <= N-1, and A and B are astronauts from the same country.
#
# Reminder: when working back and forth between python 2.7/3, don't forget that
# python < 3 requires raw_input() when reading input, while python3 is input()
#
# CONSTRAINTS
#
# 1 <= N<= 10^5
# 1 <= P <= 10^4
#
# OUTPUT FORMAT
#
# An integer that denotes the number of permissible ways to choose a pair of
# astronauts.
###############################################################################

import sys

a, b = raw_input().split(' ')
lines = int(b)
pairs=[]
singles = []
evens = []
odds = []
# We're gonna create a function to extract single values to a list, since the
# input after the initial pair gets read in as a pair of values

def nested_list_flattener(gListofLists):

    for a in gListofLists:
        if type(a) == list:
            nested_list_flattener(a)
        else:
            singles.append(a)
# We also need a way to extract the odd and even indexes from the list as part
# of our check for pairs. Since our list index starts at [0], the even indexes
# will be the first in the pairs, and the odd indexes will the be second of the
# pair. We can check for even-ness by mod 2... i.e. if index[i] % 2 == 0, it's
# even, else, it's odd
def pair_splitter(mixedList):


    count = 0
    for b in mixedList:
        if count % 2 == 0:
            evens.append(b)
        else:
            odds.append(b)
        count +=1

# Since b tells us how many lines there will be, we can create a decrement loop
# to read all the input. We split this input at the space, or ' ' to get a pair
# since the input is entered as two-space separated integers
while lines > 0:
    pairs.append(raw_input().split(' '))
    lines -= 1
nested_list_flattener(pairs)
pair_splitter(singles)
print"Lines: ", b
print("Pairs: ",pairs)
print("singles", singles)
print("Odds: ", odds)
print("Evens: ", evens)
