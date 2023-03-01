import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count=0
    x=Counter(ar)
    d={}
    for i in range(n):
        if ar[i] not in d.keys():
            d[ar[i]]=x[ar[i]]
           
    for i in d.keys():
        if d[i]%2==0:
            count=count+(d[i]//2) 
        else:
            count=count+((d[i]-1)//2)
    return count                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
