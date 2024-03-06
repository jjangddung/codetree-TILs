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
    
    for j in range(m) :
        new = arr[i]
        total += new
        temp = arr[new-1]
        arr[new-1] = new
        arr[i] = temp
    maxi = max(total,maxi)

print(maxi)