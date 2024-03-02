import sys

input = sys.stdin.readline

n = int(input())


arr = list(map(int, input().split()))

arr.sort()

mini = 10000000

for i in range(n-1) :
    result = arr[i+1] - arr[i]
    mini = min(mini,result)

print(mini)