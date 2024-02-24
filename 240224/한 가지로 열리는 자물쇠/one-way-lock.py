import sys

input = sys.stdin.readline

n = int(input())

standard_arr = list(map(int, input().split()))

count = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1,n+1) :
            if abs(i-standard_arr[0]) <= 2 or abs(j- standard_arr[1]) <= 2 or abs(k - standard_arr[2]) <= 2 :
                count +=1


print(count)