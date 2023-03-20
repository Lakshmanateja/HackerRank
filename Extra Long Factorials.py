import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    count=1
    while(n!=0):
        count=count*n
        n=n-1
    print(count)  

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
