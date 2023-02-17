e=int(input())
list1=list(map(int,input().split()))
f=int(input())
list2=list(map(int,input().split()))
count=0
for i in list1:
    if i in list2:
        count=count+1
print(count)        
