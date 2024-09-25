from sortedcontainers import SortedSet


s = SortedSet()

n,m = map(int, input().split())


# grid_lst = []

for _ in range(n) :
    x,y = map(int, input().split())
    s.add((x,y))


for _ in range(m) :
    x,y = map(int, input().split())
    
    index = s.bisect_left((x,y))

    if index == len(s) :
        print(-1,-1)
    
    else :
        x,y = s[index]
        print(x,y)