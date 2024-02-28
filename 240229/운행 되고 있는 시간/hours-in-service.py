import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

max_time = 0


for i in range(n) :
    time = [0]*10
    # print(time)
    for j in range(n) :
        if  j == i :
            print(j)
            continue
        start_time = arr[j][0]
        end_time = arr[j][1]
        for p in range(start_time,end_time) :
            time[p] = 1
    # print(time[0:11])
    max_time = max(sum(time),max_time)


print(max_time)