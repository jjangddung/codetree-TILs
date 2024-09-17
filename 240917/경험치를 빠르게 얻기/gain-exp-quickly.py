import sys


n,m = map(int, input().split())


information_lst = []

total_time = 0

for i in range(n) :
    e,t = map(int, input().split())
    total_time += t
    information_lst.append([e,t])


information_lst = [[0,0]] + information_lst
value_time = sys.maxsize
INT_MIN = -sys.maxsize

# print(information_lst)

# print(information_lst)

dp = [
    [INT_MIN]*(total_time +1 )
    
    for _ in range(n+1)
]


dp[0][0] = 0


for i in range(n+1) :
    dp[i][0] = 0


for i in range(total_time+1) :
    dp[0][i] = 0

for i in range(1,n+1) :
    exp, time = information_lst[i][0], information_lst[i][1]
    dp[i][time] = exp





for i in range(1,n+1) :
    for j in range(1,total_time +1 ) :
        exp, time = information_lst[i][0], information_lst[i][1]
        
        
        if j - time >= 0 :
            dp[i][j] = max(dp[i][j], dp[i-1][j-time] + exp)
            # print(f'i: {i}, j: {j}, exp : {exp}, time : {time}, dp  : {dp[i][j]}')

        dp[i][j] = max(dp[i-1][j], dp[i][j])

        if dp[i][j] >= m :
            value_time = min(value_time, j)



# for d in dp :
    # print(d)
# print(dp)  
# for i in range(n+1) :
    # print(dp[i][13])
if value_time == sys.maxsize :
    print(-1) 

else :
    print(value_time)