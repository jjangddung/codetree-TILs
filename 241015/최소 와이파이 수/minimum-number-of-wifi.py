import sys
import copy

# 와이파이 범위 왼쪽 바깥이 커버가 안되면 안됨
# 커버가 안되는 수간

n,m = map(int, input().split())

grid = list(map(int, input().split()))




count  = 0
for i in range(n) :
    if i-m >= 0  and grid[i-m] == 1 :
        count +=1
        if i + m + 1 >= n :
            for v in range(i-m,n) :
                grid[v] = 0
        else :
            for v in range(i-m,i+m+1) :
                grid[v] = 0


print(count)