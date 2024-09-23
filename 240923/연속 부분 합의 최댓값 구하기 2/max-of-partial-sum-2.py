import sys

n = int(input())


grid = list(map(int, input().split()))

maxi = -sys.maxsize


i = 0

prev= -sys.maxsize
while i < n :
    value = 0

    for j in range(i,n) :
        value += grid[j]
        maxi = max(value,maxi)

        if value < 0 :
            value -= grid[j]
            break
    i = j+1

print(maxi)