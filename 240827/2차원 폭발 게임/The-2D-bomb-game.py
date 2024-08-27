n,m,k = map(int , input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


# transmition>>> 폭탄을 터트림 >>> 0으로 채움 >>> 그 뒤 중력으로 내림 >>>>  mirror를 사용해 바꿈 >>> transmition 사용해서 정렬

def mirror(grid) : # 90도 회전 전
    for i in range(n//2) :
        grid[i], grid[n-1-i] = grid[n-1-i], grid[i]

def transmition(grid) :
    for i in range(n) :
        for j in range(i,n) :
            grid[i][j] , grid[j][i] = grid[j][i], grid[i][j]

def boomb(arr) :
    length = len(arr)
    start_idx= 0
    new_lst = []


    while start_idx < length :
        
        if  arr[start_idx] == 0 :
            start_idx +=1
            continue
            
       
        count = 0

        for last_idx in range(start_idx,length) :
            if arr[last_idx] == arr[start_idx] :
                count +=1

                if last_idx == length -1 :
                    # print(start_idx,new_lst)
                    if count >= m :
                        start_idx += count
                        break
                    else :
                        for t in range(start_idx,last_idx+1) :
                            new_lst.append(arr[t])
                        start_idx += count
                        break
            

            else :
                if count >= m :
                    start_idx += count 
                    break

                else :
                    for t in range(start_idx, last_idx) :
                        new_lst.append(arr[t])
                    start_idx += count
                    break

    new_lst = [0]*(n-len(new_lst)) + new_lst

    return new_lst

def mat_boomb(grid) :
    new_grid =[]

    for lst in grid :
        new_lst = boomb(lst)
        new_grid.append(new_lst)
    return new_grid

def gravitiy(grid) :
    new_grid = []

    for lst in grid :
        new_lst = []

        for l in lst :
            if l != 0 :
                new_lst.append(l)
        new_lst = [0]*(n-len(new_lst)) + new_lst
        new_grid.append(new_lst)
    
    return new_grid



for _ in range(k):
    transmition(grid)
    grid = mat_boomb(grid)
    transmition(grid)
    mirror(grid)
    # transmition(grid)
    # transmition(grid)
    grid = gravitiy(grid)
    transmition(grid)
    # grid = mat_boomb(grid)
    # print(*grid)


transmition(grid)
grid = mat_boomb(grid)
transmition(grid)


result =  0

for i in range(n) :
    for j in range(n) :
        if grid[i][j] != 0 :
            result +=1


print(result)