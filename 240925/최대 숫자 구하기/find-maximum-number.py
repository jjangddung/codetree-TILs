from sortedcontainers import SortedSet

n,m = map(int, input().split())


grid = list(map(int, input().split()))


s = SortedSet()


for i in range(1,m+1)  :
    s.add(i)


for g in grid :
    index = s.bisect_left(g)

    s.remove(s[index])
    print(s[-1])