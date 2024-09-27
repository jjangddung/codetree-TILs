import sys

from sortedcontainers import SortedSet


n,m = map(int, input().split())

grid = list(map(int, input().split()))

s = SortedSet()

for g in grid :
    s.add(g)

lst = list(map(int, input().split()))

for i in range(m) :
    order = lst[i]

    idx = s.bisect_right(order)

    if idx != 0 :
        idx -=1
        print(s[idx])
        s.remove(s[idx])
    
    else :
        print(-1)