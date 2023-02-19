from itertools import combinations_with_replacement
list1=list(input().split())
ch=sorted(list1[0])
list2=list(combinations_with_replacement(ch,int(list1[1])))
list2.sort()
for i in range(len(list2)):
    print(''.join(list2[i]))
