# dp[i]의 정의  합이 i일 때, 최소한의 동전 개수
# 합 i를 만들기 전 사용한 동전이 j번째라면,,, dp[i-matrix[j]] + 1


import sys

INT_MIN = sys.maxsize
n,m = map(int, input().split())


matrix= list(map(int, input().split()))


dp = [INT_MIN]* (m+1)


for i  in range(n) :
    coin = matrix[i]
    dp[coin] = 1



for i in range(1,m+1) :
    for j in range(n) :
        if i >= matrix[j] :
            if dp[i- matrix[j]] == INT_MIN :
                continue

            dp[i] = min(dp[i], dp[i- matrix[j]] +1 )




ans = dp[m]

if ans == INT_MIN :
    ans = -1

print(ans)