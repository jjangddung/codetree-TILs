import sys

input = sys.stdin.readline


n = int(input())


arr = [0 for _ in range(200)]

for _ in range(n) :
    k,l = map(int, input().split())
    for i in range(k+100, l+100) :
        arr[i] += 1


print(max(arr))