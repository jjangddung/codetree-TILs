import sys

input = sys.stdin.readline

n,k = map(int, input().split())

arr = list(map(int, input().split()))


max_val = 0

for i in range(n+1-k) :
    new = sum(arr[i:i+k])
    max_val = max(max_val,new)


print(max_val)