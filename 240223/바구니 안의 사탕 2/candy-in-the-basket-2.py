import sys

input = sys.stdin.readline


n, k = map(int, input().split())

arr = [0] * 101


for i in range(n) :
    num , index = map(int, input().split())
    arr[index] += num

maximum = 0
length = len(arr)

for i in range(length) :

    start =  i -k
    if i - k < 1 :
        start = 1

    end = i + k

    if i + k > 100 :
        end = 100
    
    # print(i-k,i+k-1)
    new_arr = arr[start:end+1]
    # print(new_arr)
    p = sum(new_arr)

    maximum = max(maximum,p)

print(maximum)