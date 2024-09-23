n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        # Discard both cards
        dp[i][j] = dp[i+1][j+1]
        # Discard opponent's card
        dp[i][j] = max(dp[i][j], dp[i+1][j])
        # Discard Namwoo's card
        dp[i][j] = max(dp[i][j], dp[i][j+1])
        # Card duel when Namwoo's card is less than opponent's card
        if b[j] < a[i]:
            dp[i][j] = max(dp[i][j], dp[i][j+1] + b[j])

print(dp[0][0])