import sys

n = int(input())


grid = [
    list(map(int, input().split()))

    for _ in range(n)
]


dxs, dys = [-1,0],[0,1] # 하 우

answer = [
    [sys.maxsize] *n
    for _ in range(n)
]


answer[0][0] = grid[0][0]



maxi = grid[0][0]

for i in range(1,n) :
    answer[0][i] = max(maxi,grid[0][i])
    maxi = answer[0][i]


maxi = grid[0][0]
for i in range(1,n) :
    answer[i][0] = max(maxi, grid[i][0])
    maxi = answer[i][0]




for i in range(1,n) :
    for j in range(1,n) :
        answer[i][j] = min(answer[i-1][j],answer[i][j-1])
        answer[i][j] = max(answer[i][j],grid[i][j])


print(answer[n-1][m-1])