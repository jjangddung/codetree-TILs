import sys

INT_MIN = -sys.maxsize

n = int(input())

arr =  [0]  +list(map(int, input().split()))


OFFSET = 10000

m = sum(arr)


dp = [
    [0]*(m+ 1+OFFSET)

    for _ in range(n+1)
]


def initialize():
    # 최대를 구하는 문제이므로
    # 초기값을 INT_MIN으로 넣어줍니다.
    for i in range(n + 1):
        for j in range(-m, m + 1):
            dp[i][j + OFFSET] = INT_MIN

    # 초기 조건은
    # 아직 아무런 수도 고른적이 없는 경우이므로 
    # 0번째 수까지 고려하여
    # 그룹 A 합 - 그룹 B 합이 0이고 
    # 그룹 A의 합이 0인 경우에 대한 정보 입니다.
    dp[0][0 + OFFSET] = 0



initialize()

def update(i, j, prev_i, prev_j, val):
    # 불가능한 경우 패스합니다.
    if prev_j < -m or prev_j > m or dp[prev_i][prev_j + OFFSET] == INT_MIN:
        return
    
    dp[i][j + OFFSET] = max(dp[i][j + OFFSET], dp[prev_i][prev_j + OFFSET] + val)


for i in range(1,n+1) :
    for j in range(-m,m+1) :

        update(i,j,i-1,j-arr[i],arr[i])

        update(i,j,i-1,j+arr[i],0)


if dp[n][0+OFFSET] ==0 :
    print("Yes")

else :
    print("No")