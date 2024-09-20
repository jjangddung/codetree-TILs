import sys

# 1차원 dp로도 충분히 가능한가?
# 우선 정렬을 해야할듯 하다.
# dp >>> 최대한 벌 수 있는 금액


n = int(input())

part_time = []
dp= [0]*(n)

for _ in range(n) :
    s,e,q = map(int, input().split())
    part_time.append([s,e,q])


part_time.sort(key = lambda x: x[1])

dp[0] = part_time[0][2]


def no_overlap(end,start) :
    if end < start  :
        return True
    
    return False


for i in range(1,n) :
    start = part_time[i][0]
    value = part_time[i][2]
    for j in range(i) :
        end = part_time[j][1]
        
        if no_overlap(end,start) :
            dp[i] = max(dp[j] +value , dp[i])
        
    dp[i] = max(dp[i], value)


print(max(dp))