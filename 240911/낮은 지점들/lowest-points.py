n = int(input())


d = {}

for i in range(n) :
    x,y = map(int, input().split())

    if x not in d :
        d[x] = y
    
    else :
        if y < d[x] :
            d[x] = y


total = 0

for v in d :
    total += d[v]

print(total)