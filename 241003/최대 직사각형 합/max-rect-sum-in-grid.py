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

# for g in grid :
    # for v in range(n) :
        # g[v] += 1001
# print(grid)


prefix_sum = [
    [0]*(n+1)
    for _ in range(n+1)
]

prefix_sum[0][0] = 0


# for  i in range(1,n+1) :
    # prefix_sum[1][i] = prefix_sum[1][i-1] + grid[0][i-1]
    # prefix_sum[i][1] = prefix_sum[i-1][1] + grid[i-1][0]




# 행별로 부분합 구하기

for i in range(1,n+1) :
    for j in range(1,n+1) :
        prefix_sum[i][j] = prefix_sum[i][j-1] + grid[i-1][j-1]


# 행별로 부분합을 구했음

# for p in prefix_sum :
    # print(*p)
# 
result = -sys.maxsize

# 카데인 알고리즘 적용
inf = -sys.maxsize

def kadane(temp) :
    
    max_value = inf

    
    length = len(temp)
    value_lst = [inf] * (length+1)

    for i in range(1,length) :
        
        value_lst[i] = max(value_lst[i-1]+ temp[i], temp[i])
        max_value = max(value_lst[i], max_value)
    
    return max_value





for left in range(1,n+1) :
    temp = [0]* (n+1)
    for right in range(left, n+1) :
        for row in range(1,n+1) :
            temp[row] = (prefix_sum[row][right]-prefix_sum[row][left-1])

        
        # print(temp)
        
        calc = kadane(temp)
        # print('calc: ', calc, left, right)

        result = max(calc, result)


print(result)