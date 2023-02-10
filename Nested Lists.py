if __name__ == '__main__':
    list1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list2=[]
        list2.append(name)
        list2.append(score)
        list1.append(list2)
    list3=[]  
    for i in range(len(list1)):
        list3.append(list1[i][1])
    list3.sort()
    for i in range(len(list3)):
        if list3[i]!=list3[i+1]:
            m=list3[i+1]
            break
    list4=[]    
    for i in range(len(list1)):
        if list1[i][1]==m:
            list4.append(list1[i][0])
    list4.sort()
    for i in range(len(list4)):
        print(list4[i])   
