import sys


# 요구하는 건 최소한의 중복없이 고르기
# dp[i]의 정의  >>> 중복없이  합이 i일때 최소한의 동전의 개수 

INT_MAX = sys.maxsize





n,m = map(int, input().split())

matrix = list(map(int, input().split()))

dp = [INT_MAX]* (m+1)


dp[0] = 0


for  i in range(n) :
    for j in range(m,-1,-1) :
        if j >= matrix[i] :
            if dp[j- matrix[i]] == INT_MAX :
                continue

            dp[j] = min(dp[j],dp[j-matrix[i]] +1 )


if dp[m] == INT_MAX :
    print(-1)
else :
    print(dp[m])