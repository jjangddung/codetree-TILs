import sys

input = sys.stdin.readline

n,k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

result = []

for i in range(n) :
    for j in range(i+1,n) :
        if arr[i] == arr[j] :
            if j-i <= k :
                result.append(arr[i])


print(max(result))