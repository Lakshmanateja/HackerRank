import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    len1=len(s)
    x=Counter(s)
    r=n%len1
    s1=s[:r]
    y=Counter(s1)
    return (x['a']*(n//len1))+y['a']
    #return x['a'],y['a'],s1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
