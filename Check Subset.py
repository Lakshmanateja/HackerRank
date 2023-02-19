t=int(input())
for i in range(t):
    a=int(input())
    list1=list(map(int,input().split()))
    b=int(input())
    list2=list(map(int,input().split()))
    count=0
    for j in list1:
        if j in list2:
            count=count+1
    if count==len(list1):
        print("True")
    else:
        print("False")            
