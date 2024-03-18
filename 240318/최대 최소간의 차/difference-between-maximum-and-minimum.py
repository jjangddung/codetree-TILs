import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int , input().split()))

arr.sort()

max_value = max(arr)

maxi = 10000000000000000

for min_value in range(1,max_value+1) :
    max_value  = min_value+ k
    result = 0


    for num in arr :
        if num < min_value :
            result += min_value- num
        elif max_value < num :
            result += num-max_value
    maxi = min(result,maxi)


print(maxi)