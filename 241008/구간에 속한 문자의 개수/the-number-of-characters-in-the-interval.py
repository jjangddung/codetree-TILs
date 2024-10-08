import sys

n,m,k = map(int, input().split())

str_lst = []

prefix_sum_a = [
    [0]*(m+1)
    for _ in range(n+1)
]

prefix_sum_b = [
    [0]*(m+1)
    for _ in range(n+1)
]

prefix_sum_c = [
    [0]*(m+1)
    for _ in range(n+1)
]

abc_lst = [
    [0]*(m+1)
    for _ in range(n+1)
]

for i in range(1,n+1) :
    string = str(input())

    for s in range(m) :
        if string[s] == 'a' :
            num = 1
        elif string[s] == 'b' :
            num = 2

        else :
            num = 3

        abc_lst[i][s+1] = num


# print(abc_lst)


for i in range(1,n+1):
    for j in range(1,m+1) :
        num = abc_lst[i][j]
        prefix_sum_a[i][j] = prefix_sum_a[i][j-1]
        prefix_sum_b[i][j] = prefix_sum_b[i][j-1]
        prefix_sum_c[i][j] = prefix_sum_c[i][j-1]
        if num == 1 :
            prefix_sum_a[i][j] +=   1
        
        elif num == 2 :
            prefix_sum_b[i][j] +=   1
        
        else :
            prefix_sum_c[i][j] +=   1

# print(prefix_sum_a)


for _ in range(k) :
    r1,c1,r2,c2 = map(int, input().split())
    total_a,total_b, total_c = 0,0,0

    for r in range(r1,r2+1) :
        total_a += prefix_sum_a[r][c2] - prefix_sum_a[r][c1-1]
        total_b += prefix_sum_b[r][c2] - prefix_sum_b[r][c1-1]
        total_c += prefix_sum_c[r][c2] - prefix_sum_c[r][c1-1]
    
    print(total_a,total_b,total_c)