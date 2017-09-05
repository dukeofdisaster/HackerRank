## Solution to the challenge Sparse  Arrays on hackerrank.com
#
import sys
entered =[]

# reads the first line and type casts to int
count = int(input())

# appends the next x lines into the entered array, stripping the newline character
for x in range(count):
    entered.append(sys.stdin.readline().strip())
queriesCount = int(input())
queries = []

#appends the next y lines after the queries count into an array
for y in range(queriesCount):
    queries.append(sys.stdin.readline().strip())
matchCounts = []
matchTotals = []
matches = 0
for n in range(queriesCount):
    matchTotals.append(0)
for z1 in queries:
    for z2 in entered:
        if z2 == z1:
            #matchCounts.append(matches)
            matchTotals[matches] += 1
    matches += 1


for i in matchTotals:
    print(i)
#print(matchCounts)
#print(queries)
#print(entered)
