import sys

input = sys.stdin.readline


a,b,c = map(int, input().split())
maxi = 0

for i in range(1000) :
    for j in range(1000) :
        result = i*a +j*b
        if result > c :
            break
        maxi = max(result,maxi)

print(maxi)