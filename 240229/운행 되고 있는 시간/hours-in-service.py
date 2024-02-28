import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

max_time = 0

time = [0]*1001
for i in range(n) :
    for j in range(n) :
        if  i == j :
            continue
        start_time = arr[j][0]
        end_time = arr[j][1]
        for i in range(start_time,end_time) :
            time[i] = 1
        max_time = max(sum(time)-1,max_time)


print(max_time)