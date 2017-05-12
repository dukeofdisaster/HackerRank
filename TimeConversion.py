###############################################################################
# TIME CONVERSION
# Given a time in 12-hour am/pm format, convert it to military (24-hr) time.
#
# INPUT FORMAT
# A single string containing a time in 12-hour clock format (hh:mm:ssAM or
# hh:mm:ssPM) wehre 01 <= hh <= 12 and 00 <= mm, ss <= 59
#
# OUTPUT FORMAT
# Convert and print given time in 24hr format where 00 <= hh <= 23
###############################################################################
# Note: We have several options for figuring out how to tackle this problem. At
# first look it might seem like we can use the 're' library, to find a matching
# sequence in the time string, i.e. "AM" or "PM"...which is nice, but also more
# complicated than we need the problem to be.
#
# We've seen that HackerRank likes to use the split() function, what if we used
# it ourselves to split our time string into 3 separate strings, based on the
# fact that the format of the string is somewhat split itself by the colon ':'?
#
# This method works. We can declare multiple variables in the same line by
# using commas, so a,b,c = time.split(':') works just fine because splitting
# the time string by the two colons creates 3 separate substrings.The first two
# of these substrings will be easy to work with because they are numbers, so
# type casting them with int() will be easy.but the last string still contains
# AM or PM. How can we separate the numbers from the letters?

# The next useful method will be slicing. we can slice a string x using the
# format: myString[int:int], which will create a substring from the left value
# to the right value based on what you give the string. [:2] will return the
# first two values of the string, while [2:] will return the values between the
# second character all the way to the end of the string... i.e. all but the 1st
# two. so we can create two sub values from the c string by slicing and storing
# these values as aORp (am or pm) and seconds.
import sys


time = raw_input().strip()

a,b,c = time.split(':')
aORp = c[2:]
seconds= c[:2]

if aORp[0] == 'A':
    if a == '12':
        print('00'+':'+b+':'+seconds)
    else:
        print(a+':'+b+':'+seconds)

# For PM, we use two type casts: first we typecast a to an int so we can
# do the conversion to 24 time, which consists of adding 12 to the time
elif aORp[0] == 'P':
    if a == '12':
        print (a+':'+b+':'+seconds)
    else:
        print(str((int(a)+12))+':'+b+':'+seconds)

