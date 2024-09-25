from sortedcontainers import SortedSet


n,k =  map(int, input().split())


grid = list(map(int, input().split()))


grid = set(grid)

s = SortedSet()


for num in grid :
    s.add(num)


for t in range(k) :
    print(s[-1], end= " ")
    s.remove(s[-1])