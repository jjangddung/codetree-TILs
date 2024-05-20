n = int(input())

order = 0


# grid의 좌표가 0

grid = [list(map(int , input().split())) for _ in range(n)]


visited = [[0]* n for _ in range(n)]

answer = [[0]* n for _ in range(n)]



def in_range(x,y) :
    return  0 <=x <n and 0 <= y < n 

def can_go(x,y) :
    if  not in_range(x,y) :
        return False
    
    if visited[x][y] or grid[x][y] == 0 :
        return False
    
    return True


def dfs(x,y) :
    global order

    dxs, dys = [-1,0,1,0] , [0,1,0,-1]


    for dx , dy in zip(dxs, dys) :
        new_x, new_y = x + dx , y +dy
        
        if can_go(new_x,new_y) :
            answer[new_x][new_y] = order
            visited[new_x][new_y] = 1
            dfs(new_x,new_y)


for x in range(n) :
    for y in range(n) :
        if visited[x][y] == 0 and grid[x][y] == 1 :
            order +=1            
            dfs(x,y)
            


result_list = [0]*(order+1)

for p in range(1,order+1) :
    for x in range(n) :
        for y in range(n) :
            if answer[x][y] == p :
                result_list[p] += 1


new_result_list = result_list[1:]

print(len(new_result_list))
new_result_list.sort()
for alpha in new_result_list :
    print(alpha)