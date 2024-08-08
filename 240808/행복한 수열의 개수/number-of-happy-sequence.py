import sys

input = sys.stdin.readline



n,m = map(int, input().split())

matrix= [list(map(int, input().split())) for _ in range(n)]


ans = 0

for i in range(n) :
    horizon = matrix[i]
    # print(horizon)

    count = 1
    maxi =  1
    # step = 0

    for k in range(1,n) :
        if horizon[k] == horizon[k-1] :
            # print("k: ",k)
            # step +=1
            count +=1
            # print("count: " , count)
            maxi = max(count, maxi)
        
        else :
            maxi = max(count, maxi)
            count = 1

    # print(maxi)
    # print("Step: ", step)

    

    if maxi >= m :
        ans +=1
    


for i in range(n) :
    vertical = []

    count =1
    maxi = 1
    for j in range(n) :
        ver = matrix[j][i]
        vertical.append(ver)
    # print(vertical)

    
    for k in range(1,n) :
        if vertical[k] == vertical[k-1] :
            count +=1
            maxi = max(count, maxi)
        
        else :
            maxi = max(count, maxi)
            count = 1

    if maxi >= m :
        ans +=1



print(ans)