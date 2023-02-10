if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list1=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k!=n:
                    list2=[]
                    list2.append(i)
                    list2.append(j)
                    list2.append(k)
                    list1.append(list2)
    print(list1)   
