import sys

# 카데인 알고리즘을 적용한다면...?

# 업데이트 방향을 어떻게...?
# prefix_sum = []

# 앞에선 prefix_sum을 쓰고 뒤에서 DP를 활용할 방법은 없을까?




n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

for g in grid :
    for v in range(n) :
        g[v] += 1001
# print(grid)


prefix_sum = [
    [0]*(n+1)
    for _ in range(n+1)
]

prefix_sum[0][0] = 0


for  i in range(1,n+1) :
    prefix_sum[1][i] = prefix_sum[1][i-1] + grid[0][i-1]
    prefix_sum[i][1] = prefix_sum[i-1][1] + grid[i-1][0]






for i in range(1,n+1) :
    for j in range(1,n+1) :
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + grid[i-1][j-1] - prefix_sum[i-1][j-1]


result = -sys.maxsize


# for p in prefix_sum :
    # print(*p)

for x1 in range(1,n+1) :
    for y1 in range(1,n+1) :
        for x2 in range(x1,n+1) :
            for y2 in range(y1,n+1) :
                value = prefix_sum[x2][y2] -\
                        prefix_sum[x2][y1-1] -\
                        prefix_sum[x1-1][y2] +\
                        prefix_sum[x1-1][y1-1]


                value -= (1001)*(x2-x1+1)*(y2-y1+1)
                # if value == 900 :
                    # print(f'x1: {x1} , y1 : {y1}, x2:{x2}, y2:{y2}, value: {value}') 
                result = max(result,value)

print(result)