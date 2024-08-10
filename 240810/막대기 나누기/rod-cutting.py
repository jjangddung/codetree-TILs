import sys

input = sys.stdin.readline

# dp의 정의를 어떻게 해아할지 ...
# dp[i]는 길이가 i일 때의  최대의 값

n = int(input())


matrix = list(map(int , input().split()))

INT_MIN = - sys.maxsize

dp = [0] *  (n+1)


for i in range(n) :
    for j in range(1,n+1) :
        if (i+1) <=  j :
            if dp[j-i-1] == INT_MIN :
                continue

            dp[j] = max(dp[j], dp[j-i-1]+ matrix[i])


print(max(dp))