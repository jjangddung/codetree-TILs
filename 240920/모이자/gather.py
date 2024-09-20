import sys


n = int(input())

grid = list(map(int,input().split()))


distance = sys.maxsize


for i in range(n) :
    dis = 0

    for j in range(n) :
        dis += abs(grid[j]) * abs(j-i)
    
    distance = min(dis,distance)

print(distance)