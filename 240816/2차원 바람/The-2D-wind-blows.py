n,m,q = map(int, input().split())


matrix = [list(map(int, input().split())) for _ in range(n)]




def can_go(x,y) :
    return r1-1 <=x < r2 and c1-1 <= y < c2

def sum_go(x,y) :
    return 0 <=x < n and 0 <= y < m 

for _ in range(q) :
    r1,c1,r2,c2 = map(int, input().split())
    new_x, new_y = r1-1,c1-1
    dxs, dys = [0,1,0,-1] , [1,0,-1,0] # 우하좌상
    changing = []
    nums = []

    count = 0
    prev = matrix[new_x][new_y]
    while count < 4 :
        c_x, c_y = new_x+ dxs[count],new_y + dys[count]

        if can_go(c_x,c_y) :

            new_x,new_y =c_x,c_y
            temp = matrix[new_x][new_y]
            matrix[new_x][new_y] = prev # 이전값
            # print(prev)
            prev = temp
            # changing.append([new_x,new_y])

        else :
            count +=1
    
    # print(*matrix)

    for x in range(r1-1,r2) :
        for y in range(c1-1,c2) :
            total = matrix[x][y]
            t  = 1

            for dx, dy in zip(dxs,dys) :
                p,q = x +dx , y + dy
                if sum_go(p,q) :
                    t +=1
                    total += matrix[p][q]

            num = total//t
            nums.append(num)
    i = 0

    for x in range(r1-1,r2) :
        for y in range(c1-1,c2) :
            
            matrix[x][y] = nums[i]
            i +=1

    


    


for i in range(n) :
    print(*matrix[i])