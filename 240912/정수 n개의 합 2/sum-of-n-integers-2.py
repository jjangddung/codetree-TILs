import sys


n,k = map(int, input().split())

grid = list(map(int, input().split()))

s = [0]*(n+1)


for i in range(n) :
    s[i+1] = s[i] + grid[i]


maxi = -sys.maxsize

# print(s)

for t in range(2,n+1) :
    result = s[t] - s[t-k]
    # print(result)
    maxi = max(result,maxi)

print(maxi)