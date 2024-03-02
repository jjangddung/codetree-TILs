import sys

input = sys.stdin.readline


n,m = map(int, input().split())

maxi = 0


for i in range(n,m+1) :
    ele = str(i)

    count = 0

    for j in range(len(ele)) :
        element = int(ele[j])
        count += element
    maxi = max(maxi,count)


print(maxi)