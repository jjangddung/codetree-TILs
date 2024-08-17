import sys



input = sys.stdin.readline




n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

r,c,m1,m2,m3,m4,direct = map(int , input().split())
r -=1
c -=1
# print(r,c)
# if direct = 0 :
    # prev_x, prev_y = r + dxs[1] , c + dys[1]
# 
# else :
    # prev_x, prev_y = r + dys[0] , c + dys[0]
# 
# prev= grid[prev_x][prev_y]


# for _ in grid :
    # print(*_)
# 
# print()
# print()
prev = grid[r][c]




if direct == 0 :
    dxs, dys = [-1,-1,1,1] , [1,-1,-1,1] # (우상),(좌상),(좌하),(우하)
else :
    dxs, dys = [-1,-1,1,1] , [-1,1,1,-1] # (좌상),(우상),(우하),(좌하)
    m1,m2,m3,m4 = m2,m1,m4,m3

count = 0
t1,t2,t3,t4 = 0,0,0,0
while t1 < m1 :
    r,c = r + dxs[count], c + dys[count]
    temp = grid[r][c]
    grid[r][c] = prev
    prev =  temp
    t1 +=1
count +=1
while t2 < m2 :
    r,c = r + dxs[count] , c + dys[count]
    # print(r,c)
    temp = grid[r][c]
    grid[r][c] = prev
    prev =  temp
    t2 +=1
count +=1
while t3 < m3 :
    r,c = r + dxs[count], c + dys[count]
    # print(r,c)
    temp = grid[r][c]
    grid[r][c] = prev
    prev =  temp
    t3 +=1
count +=1
while t4 < m4 :
    # print(r,c)
    r,c = r + dxs[count] , c + dys[count]
    # print(r,c)
    temp = grid[r][c]
    grid[r][c] = prev
    prev =  temp
    t4 +=1


for _ in grid :
    print(*_)