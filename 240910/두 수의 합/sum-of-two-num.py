n,k = map(int, input().split())


grid = list(map(int, input().split()))
grid.sort()

d = {}


for i in range(n) :
    
    if not grid[i] in d :
        d[grid[i]] = 1
    
    else :
        d[grid[i]] +=1
    


count =  0

for v in d :
    if k-v not in d :
        continue
    
    if k-v < v :
        continue
    
    elif k-v == v :
        count += (d[v]*(d[v]-1)/2)
    
    else :
        count  += d[v]* d[k-v]

print(count)