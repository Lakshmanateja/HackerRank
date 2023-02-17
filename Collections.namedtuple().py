n=int(input())
list1=list(input().split())
count=0
for i in range(n):
    count=count+int(list(input().split())[list1.index('MARKS')])
print(count/n)
