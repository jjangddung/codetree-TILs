import sys

input = sys.stdin.readline

N = int(input())
sum = 0

k = N


for i in range(1, N+1) :
    k = k//i
    sum += 1

    if k <= 1:
        print(sum)
        break