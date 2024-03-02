import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

count = 0
for num in range(n) :
    if arr[num] == 2 :
        count +=1
    if count == 3 :
        print(num+1)
        break