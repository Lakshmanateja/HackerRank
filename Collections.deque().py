from collections import deque
n=int(input())
d=deque()
for i in range(n):
    s1=input().split()
    if s1[0]=="append":
        d.append(int(s1[1]))
    elif s1[0]=="appendleft":
        d.appendleft(int(s1[1]))
    elif s1[0]=="pop":
        d.pop()
    elif s1[0]=="popleft":
        d.popleft()
list1=list(d)
for i in range(len(list1)):
    print(list1[i],end=" ")
