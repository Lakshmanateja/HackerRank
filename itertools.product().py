from itertools import product 
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list3=list(product(list1,list2))
for i in range(len(list3)):
    print(list3[i],end=" ")
