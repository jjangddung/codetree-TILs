import sys

n,m = map(int, input().split())


grid = [
    list(map(str, input().split()))
    for _ in range(n)
]

count = 0
start = grid[0][0]
end = grid[n-1][m-1]
for i in range(1,n-2) :
    for j in range(1,m-2) :
        for k in range(i+1,n-1):
            for l in range(j+1,m-1) :
                if grid[i][j] != start :
                    if grid[k][l] == start :
                        count +=1

print(count)