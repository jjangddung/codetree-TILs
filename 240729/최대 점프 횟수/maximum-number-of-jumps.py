import sys

input = sys.stdin.readline


INT_MIN = - sys.maxsize


n = int(input())


matrix=  list(map(int, input().split()))


dp = [INT_MIN] *n

dp[0] = 0



for i in range(1,n) :
    for j in range(i) :
        if dp[j] == INT_MIN :
            continue


        if j + matrix[j] >= i :
            dp[i] = max(dp[j] +1 , dp[i])


print(max(dp))