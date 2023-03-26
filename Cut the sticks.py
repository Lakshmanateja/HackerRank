import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    x=Counter(arr)
    list1=list(x.keys())
    list1.sort()
    sort_x={i:x[i] for i in list1}
    list2=[]
    for i in sort_x.values():
        list2.append(i)
    list3=[len(arr)]
    for i in range(1,len(list2)):
        list3.append(list3[i-1]-list2[i-1]) 
    return list3    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
