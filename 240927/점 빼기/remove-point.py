# from sortedcontainers import Sortedset
from sortedcontainers import SortedSet
import sys



n,m = map(int, input().split())

s = SortedSet()


for _ in range(n) :
    x,y = map(int, input().split())
    s.add((x,y))



# print(s)

for _ in range(m) :
    order = int(input())

    idx = s.bisect_left((order,-1))
    if idx == len(s) :
        print(-1,-1)
    
    else :
        print(s[idx][0],s[idx][1])
        s.remove(s[idx])