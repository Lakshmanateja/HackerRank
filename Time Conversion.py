import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    list1=[i for i in s]
    if list1[8]=='P':
        if list1[0]=='1' and list1[1]=='2':
            s2=s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
            return s2
        s1=list1[0]+list1[1]
        ints=int(s1)
        ints=ints+12
        strs=str(ints)
        s2=strs+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
        return s2
    else:
        if list1[0]=='1' and list1[1]=='2':
            s2='0'+'0'+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
            return s2
        s2=s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
        return s2              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
