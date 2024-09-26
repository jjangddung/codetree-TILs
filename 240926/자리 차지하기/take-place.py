from sortedcontainers import SortedSet


n,m = map(int, input().split())

grid = list(map(int, input().split()))



maxi = 0
s =  SortedSet()
# count = 0
for i in range(n) :
    t= grid[i]
    while t >  0 and t  in s : 
        t -=1

    if t == 0 :
        break
    
    else :
        s.add(t)

print(len(s))