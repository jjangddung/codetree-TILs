import sys

input = sys.stdin.readline


n = int(input())



dp = [0]*10001


#3*X + 2*y = i


dp[2] = 1
dp[3] = 1
dp[4] = 1
dp[5] = 2
# dp[6] = 2 # 3+3 , 2+2+2
# dp[7] = 3 # 3+2+2
# dp[8] = 4  # 3+3+2 , 2+2+2+2 , 
# dp[9] = 5   #3+3+3,2+2+2+3



for i in range(5,n+1) :
    dp[i] += dp[i-2] 
    dp[i] += dp[i-3]  

print(dp[n])