import sys

input = sys.stdin.readline


n = int(input())


arr = []

for _ in range(n) :
    k = int(input())

    arr.append(k)



cnt = 1

for i in range(1,n) :
    if arr[i] != arr[i-1] :
        cnt +=1



print(cnt)