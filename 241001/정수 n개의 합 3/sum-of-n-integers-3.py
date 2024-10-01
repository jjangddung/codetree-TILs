import sys

# 0,0에서부터 그냥 누적합 다 더하고 maximum 밸류는 나중에 찾기

n,k = map(int, input().split())

grid = [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]

grid = [[0]*n] + grid


prefix_sum = [
    [0]*(n+1)
    for _ in range(n+1)
]


def initiatialize() :
    for t in range(n) :
        prefix_sum[t][0] = 0
        prefix_sum[0][t] = 0


initiatialize()

for i in range(1,n+1) :
    for j in range(1,n+1) :
        prefix_sum[i][j] = prefix_sum[i-1][j] + \
                           prefix_sum[i][j-1] - \
                           prefix_sum[i-1][j-1] +  grid[i][j]


# print(prefix_sum)

result = -sys.maxsize
for i in range(k,n+1) :
    for j in range(k,n+1) :
        value = prefix_sum[i][j] - \
                prefix_sum[i][j-k] -\
                prefix_sum[i-k][j] + \
                prefix_sum[i-k][j-k]
        result = max(value, result)
        # print(value)



print(result)