import sys

input = sys.stdin.readline


n = int(input())


arr = []

while True:
    if n < 2:
        arr.append(n)
        break

    arr.append(n % 2)
    n //= 2



for i in arr[::-1] :
    print(i, end ="")