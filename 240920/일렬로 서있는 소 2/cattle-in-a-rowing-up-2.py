import sys

n = int(input())

grid = list(map(int, input().split()))


count = 0
for i in range(n) :
    for j in range(i+1,n) :
        for k in range(j+1, n) :
            if grid[i] <= grid[j] and grid[j] <= grid[k] :
                count +=1


print(count)