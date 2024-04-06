import sys

input = sys.stdin.readline

n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1,0,1,0] # 상 우 하 좌
dys = [0,1,0,-1] 


def in_range(x,y) :
    return 0 <=  x < n and 0<= y < m 

comb = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]] # 나올 수 있는 조합
maximum = 0

for x in range(n) :
    for y in range(m) :
        for com in comb :
            nx_1, ny_1 = x + dxs[com[0]], y + dys[com[0]]
            nx_2, ny_2 = x + dxs[com[1]], y + dys[com[1]]

            if  not in_range(nx_1,ny_1) or not in_range(nx_2,ny_2):
                continue
            result = matrix[x][y] + matrix[nx_1][ny_1] + matrix[nx_2][ny_2]
            maximum = max(result, maximum)


print(maximum)