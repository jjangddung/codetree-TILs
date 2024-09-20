# 증가하는 dp 따로  ~i번째를 반드시 포함한 것에서 찾기>
# 감소하는 dp 따로... ?  i번째부터 ~~ 끝까지 >>>> 리버스로 바꾸면 되나..?


n = int(input())

grid = list(map(int, input().split()))
new_grid = grid[::-1]

up_dp = [1]*(n)
down_dp = [1]*n


for i in range(1,n) :
    for j in range(i) :
        if grid[i] > grid[j] :
            up_dp[i] = max(up_dp[j]+1, up_dp[i])
        
        # elif grid[i] < grid[j] :
            # down_dp[i] = max(down_dp[j]+1, down_dp[i])


for i in range(1,n) :
    for j in range(i) :
        if new_grid[j] < new_grid[i] :
            down_dp[i] = max(down_dp[j]+1, down_dp[i])
# print(up_dp)
# print(down_dp)
# print("origin: " ,grid)
# print("reverse : ", new_grid)

result = 0
for i in range(n) :
    maxi = up_dp[i] + down_dp[n-i-1] - 1
    result = max(maxi, result)

print(result)