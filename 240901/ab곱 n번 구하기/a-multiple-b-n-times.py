n = int(input())


lst = [list(map(int , input().split())) for _ in range(n)]

# print(lst)
for i in range(n) :
    a = lst[i][0]
    b = lst[i][1]
    value = 1

    for t in range(a,b+1) :
        value *= t
    print(value)