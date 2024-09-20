# 겹치지 않는다는 걸 어떻게 구현할 수 있을까
# dp[i]를 끝점 기준으로 정렬시켰을 때, i번째를 꼭 포함해 최대 선분 길이로 정의한다면...?
# dp[i] =   
#    k에 대해서       안겹침 max(dp[i-k] + 1,dp[i])
#                       겹침 max(dp[i-k],dp[i]) 겹치는 경우는 빼고 생각해야 안겹치는 케이스에 대해서만 출력
n = int(input())

line_lst = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [0]*(n) 


line_lst.sort(key = lambda x: x[1])

dp[0] = 1



def no_overlap(x1,y1,x2,y2) :
    if x2 > y1 :
        return True
    return False

for i in range(1,n) :
    x2,y2 = line_lst[i]
    for j in range(i) :
        x1,y1 = line_lst[j]
        if no_overlap(x1,y1,x2,y2) :
            dp[i] = max(dp[j]+1, dp[i])


print(max(dp))