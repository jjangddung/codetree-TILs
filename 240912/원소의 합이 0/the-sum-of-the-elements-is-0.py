import sys

a,b,c,d ={},{},{},{}

maxi = 0

n = int(input())

num_lst = [
    list(map(int, input().split()))
    for _ in range(4)
]

d = {}



for i in range(n) :
    for j in range(n) :
        diff = num_lst[0][i] + num_lst[1][j]

        if diff not in d :
            d[diff] = 1
        
        else :
            d[diff] += 1


count = 0


for i in range(n) :
    for j in range(n) :
        new = -(num_lst[2][i] + num_lst[3][j])

        if new in d :
            count += d[new]
        

print(count)