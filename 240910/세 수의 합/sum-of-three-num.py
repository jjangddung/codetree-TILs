import sys

n,m = map(int, input().split())

grid = list(map(int, input().split()))

grid.sort()

d = {}

for i in range(n) :
    v = grid[i]

    if v not in d :
        d[v] =1
    
    else :
        d[v] +=1


# print(d)
# i,j,k 세 가지 value 뽑기
count = 0
for i in d :
    for j in d :
        if j < i :
            continue
        for k in d :
            if k < j :
                continue
            if i + j + k  != m :
                continue

            # print(i,j,k)
            if i == j and j != k :
                count += d[k]*d[i]*(d[i]-1)//2
                # print("1: ")
            
            elif i != j and j == k :
                count += d[i]*d[j]*(d[j]-1)//2
            
            elif i == j ==  k :
                count += d[i]*d[i-1]*d[i-2]//6
            
            else :
                count += d[i]*d[j]*d[k]
            # print(count)


print(count)