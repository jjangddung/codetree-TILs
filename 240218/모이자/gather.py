import sys

input = sys.stdin.readline


n = int(input())

arr =list(map(int, input().split()))


min_dis = []

for i in range(n) :
    result = 0
    for j in range(n) :
        number = arr[j]
        dis = abs(i-j)
        result += dis*number
    min_dis.append(result)

print(min(min_dis))