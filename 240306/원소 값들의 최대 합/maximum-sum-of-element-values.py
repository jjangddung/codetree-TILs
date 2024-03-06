import sys

input  = sys.stdin.readline


n,m = map(int , input().split())

ori_arr = list(map(int , input().split()))

maxi = 0

for i in range(n) :
    arr = []
    for k in range(n) :
        arr.append(ori_arr[k])
    
    total = 0
    first = arr[i]
    total += first
    for j in range(m-1) :
        if j == 0 :
            new = arr[first-1]
        else :
            new = arr[new-1]
        total += new
    maxi = max(total,maxi)

print(maxi)