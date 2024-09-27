import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline


n,m = map(int, input().split())

grid = [
    int(input())
    for _ in range(n)
]



s = SortedSet()


for i in range(n) :
    for j in range(i+1,n) :
        result = abs(grid[i] -grid[j])

        if result >= m :
            if result == m :
                s.add(result)
                break
            s.add(result)


if len(s) != 0 :
    print(s[0])

else :
    print(-1)