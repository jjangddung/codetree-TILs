import sys


input = sys.stdin.readline


n, k = map(int, input().split())



arr = [0 for _ in range(n)]


for i in range(k) :
    start, end = map(int, input().split())

    for j in range(start-1, end) :
        arr[j] += 1


print(max(arr))