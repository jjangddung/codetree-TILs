import sys

n,m = map(int, input().split())


# 체킹된 좌표보다 낮은 좌표 한해서 출발 시켜야함



grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


dp = [
    [-1]*m
    for _ in range(n)
]



dp[0][0] = 1

count = 1
for i in range(n) :
    for j in range(m):
        for p in range(i) :
            for q in range(j) :
                if dp[p][q] == -1 :
                    continue
                if grid[p][q] < grid[i][j] :
                    dp[i][j] = max(dp[p][q]+1, dp[i][j])
                    # print(i,j,p,q)
        
        count = max(count, dp[i][j])


# print(*dp, sep = "\n")
print(count)