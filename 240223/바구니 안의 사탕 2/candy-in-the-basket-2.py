import sys

input = sys.stdin.readline


n, k = map(int, input().split())

arr = [0] * 1000001


for i in range(n) :
    num , index = map(int, input().split())
    arr[index] = num

maximum = 0

length = len(arr)
for i in range(k,length-k) :
    # print(i-k,i+k-1)
    new_arr = arr[i-k:i+k+1]
    # print(new_arr)
    p = sum(new_arr)

    maximum = max(maximum,p)

print(maximum)