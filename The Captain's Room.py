from collections import Counter
k=int(input())
list1=list(map(int,input().split()))
x=Counter(list1)
for i in x.elements():
    if x[i]==1:
        print(i)
        break
