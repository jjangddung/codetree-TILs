import sys

INT_MIN = -sys.maxsize

matrix = [1, 2, 5]
coin = [1 ,2,9]
n = int(input())

dp = [INT_MIN] * (n + 1)

# 초기 값 설정
dp[0] = 1


# DP 배열 업데이트
for i in range(1, n + 1):
    for j in range(3):
        if dp[i-matrix[j]] != INT_MIN :
            if j == 0  :
                dp[i] = 0

            dp[i] += dp[i-matrix[j]]


# 결과 출력
print(dp[n]%10007)