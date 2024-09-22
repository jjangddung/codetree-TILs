import sys

n = int(input())
INT_MIN = -sys.maxsize
grid = [0] + list(map(int, input().split()))

# dp[i][j]: i번째까지의 계단 도달 시 j번만큼 1칸씩 움직였을 때의 최대 동전 개수
dp = [[INT_MIN] * 4 for _ in range(n + 1)]

# 초기값 설정
dp[0][0] = 0

maxi = INT_MIN
for i in range(1, n + 1):
    for j in range(4):
        # 1칸 오르는 경우
        if j > 0 and i - 1 >= 0 and dp[i - 1][j - 1] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + grid[i])
        
        # 2칸 오르는 경우
        if i - 2 >= 0 and dp[i - 2][j] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + grid[i])

        # 최대값 업데이트
        maxi = max(maxi, dp[i][j])

# print(dp)
print(maxi)