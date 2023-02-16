from itertools import permutations
list2=list(map(str,input().split()))
s=list2[0]
n=list2[1]
list1=list(permutations(s,int(n)))
list1.sort()
for i in range(len(list1)):
    for j in range(0,int(n)):
        print(list1[i][j],end="")
    print()    
