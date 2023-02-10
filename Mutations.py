def mutate_string(string, position, character):
    list1=[i for i in string]
    list1[position]=character
    x=""
    for i in range(len(list1)):
        x=x+list1[i]
    return x

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
