import sys

input = sys.stdin.readline


n,h,t = map(int, input().split())


arr = list(map(int, input().split()))


# avg를 구한 후 avg와 가까운 구간 찾기

minimum = 1000000

ele = min(10,n)
for p in range(t,t+1) :
    for i in range(n-p+1) :
        new_arr = arr[i:i+p]
        # print(new_arr)
        total = 0

        for i in new_arr :
            total += abs(i-h)

        # print(total)

        minimum = min(total,minimum)


print(minimum)