import math
import os
import random
import re
import sys
#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min1=0
    max1=0
    list1=[scores[0]]
    for i in range(1,len(scores)):
        if scores[i]>max(list1):
            max1=max1+1
        if scores[i]<min(list1):
            min1=min1+1
        list1.append(scores[i])    
    list2=[]
    list2.append(max1)
    list2.append(min1)
    return list2         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

