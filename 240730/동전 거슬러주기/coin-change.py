import sys

INT_MAX = sys.maxsize
n, m = map(int, input().split())

matrix = list(map(int, input().split()))

dp = [INT_MAX] * (m + 1)
dp[0] = 0  # 합이 0일 때는 동전이 필요하지 않음

for i in range(n):
    coin = matrix[i]
    if coin <= m:
        dp[coin] = 1

for i in range(1, m + 1):
    for j in range(n):
        if i >= matrix[j]:
            if dp[i - matrix[j]] != INT_MAX:
                dp[i] = min(dp[i], dp[i - matrix[j]] + 1)

ans = dp[m]

if ans == INT_MAX:
    ans = -1

print(ans)