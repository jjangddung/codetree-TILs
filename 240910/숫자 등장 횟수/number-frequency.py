n, m = map(int, input().split())

grid = list(map(int, input().split()))

num_s = list(map(int, input().split()))


d = {}

for v in grid :
    if v not in d :
        d[v] = 1
    else :
        d[v] = d[v] +1




for num in num_s :
    if num not in d :
        print(0, end=" ")
    else :
        print(d[num], end= " ")