import sys

input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split()))
maxi = 0

for k in range(1,101):
    count = 0
    for i in range(n-1) :
        for j in range(i+1,n) :
            if 2*k == arr[i] + arr[j] :
                count +=1
    maxi = max(count,maxi)

print(maxi)