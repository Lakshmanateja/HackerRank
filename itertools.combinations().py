from itertools import combinations
list1=input().split()
str1=list1[0]
k=int(list1[1])

for i in range(1,k+1):
    for j in combinations(sorted(str1),i):
        print(''.join(j)) 

