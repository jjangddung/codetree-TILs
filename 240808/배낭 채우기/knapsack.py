import sys

n, m = map(int, input().split())


jew_list = [list(map(int, input().split())) for _ in range(n)]


mini = -sys.maxsize
dp = [mini]*(m+1)

dp[0] = 0

# 중복이 고려가 안됨 중복을 고려하도록 해야한다.
# for문을 거꾸로 돌리면 중복이 고려도미

for i in range(n) :
    for j in range(m,-1,-1) :
        weight = jew_list[i][0]
        value = jew_list[i][1]
        if weight <= j :
            if dp[j-weight] < 0  :
                continue

            dp[j] = max(dp[j], dp[j-weight] + value)



print(max(dp))