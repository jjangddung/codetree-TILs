import sys

input = sys.stdin.readline


n = 6

arr = list(map(int, input().split()))

total_sum = sum(arr)
result = 10000000


for i in range(n-2) :
    for j in range(i+1,n-1) :
        for k in range(j+1,n) :
            sum_1 = arr[i] + arr[j] + arr[k]
            sum_2 = total_sum - sum_1
            mid = abs(sum_1-sum_2)
            result = min(result, mid)


print(result)