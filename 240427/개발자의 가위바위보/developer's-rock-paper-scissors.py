n = int(input())
comp_list = [list(map(int, input().split()))for i in range(n)]

crp_list  = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
maxi = 0

for rcp in crp_list :
    count = 0
    for comp in comp_list :
        first = rcp.index(comp[0])
        second = rcp.index(comp[1])
        if first - second == 1 or first - second == -2 :
            count +=1
    maxi = max(count, maxi)


print(maxi)