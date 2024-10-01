import sys


n,m = map(int, input().split())
grid = list(map(int, input().split()))


# prefix_sum[i][j] 마지막 원소가 i일때 길이가 j일때의 합

inf = -sys.maxsize
inf = -10
prefix_sum = [
    [inf]*(n+1)
    for _ in range(n+1)
]


prefix_sum[0][0] = 0

count  = 0

for i in range(1,n+1) :
    for j in range(1,n+1) :

        if j == 1 :
            prefix_sum[i][j] = grid[i-1]
        if prefix_sum[i-1][j-1]  == inf :
            continue

        prefix_sum[i][j] = prefix_sum[i-1][j-1] + grid[i-1]

        if prefix_sum[i][j] == m :
            count+=1


# print(prefix_sum)
print(count)