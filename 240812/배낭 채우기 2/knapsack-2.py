import sys


n,m = map(int, input().split())


#중복을 허용하는 상황에서의 작성 방법..
# dp[i]는 그 무게일때의 value의 합들 (w,v)
jew_list = [list(map(int , input().split())) for _ in range(n)]

dp = [-1]*(m+1)

dp[0] = 0 



for i in range(n) :
    for j in range(1,m+1) :
        value,weight = jew_list[i][1], jew_list[i][0]
        if weight <= j :
            if dp[j-weight] == -1 :
                continue

            dp[j] = max(dp[j], dp[j-weight]+ value)


print(max(dp))