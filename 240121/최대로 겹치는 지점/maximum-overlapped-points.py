import sys

input = sys.stdin.readline


n = int(input())


arr = [0 for _ in range(0,101)]

for _ in range(n) :
    k,l = map(int, input().split())
    for i in range(k, l+1) :
        arr[i] += 1


print(max(arr))