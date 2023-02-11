import textwrap

def wrap(string, max_width):
    s=""
    m=len(string)%max_width
    for i in range(0,len(string)-max_width-m+1,max_width):
        for j in range(i,i+max_width):
            s=s+string[j]
        s=s+"\n"  
    for i in range(len(string)-m,len(string)):
        s=s+string[i]     
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
