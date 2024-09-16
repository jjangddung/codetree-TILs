import sys

# dp로 구현하는 방법
n = int(input())


lst = list(map(int, input().split()))
# print(lst)
lst = sorted(lst)

# print(lst)
total_sum = sum(lst)
dp = [
    [False]*(total_sum//2 +1)
    for _ in range(n+1)
]

for i in range(n) :
    dp[i][0] = True




result = sys.maxsize



for i in range(1,n+1) :
    for j in range(1,total_sum//2 +1 ) :
        if lst[i-1] <= j :
            dp[i][j] = dp[i-1][j] or dp[i-1][j-lst[i-1]]
        
        else :
            dp[i][j] = dp[i-1][j]

        
        if dp[i][j] :
            result = min(abs(total_sum/2-j), result)


print(int(result))