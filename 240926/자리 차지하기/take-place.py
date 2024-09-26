from sortedcontainers import SortedSet


n,m = map(int, input().split())

grid = list(map(int, input().split()))



maxi = 0
s =  SortedSet()
count = 0
for i in range(n) :
    t= grid[i]
    while True :
        if t == 0   :
            maxi = max(len(s),maxi)
            count +=1
            break
        if t not in s :
            s.add(t)
            break
        
        else :
            t -=1
    
    if count != 0 :
        break
    maxi = max(len(s),maxi)

print(maxi)