import sys


input = sys.stdin.readline


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
answer = []


count = 0
bomb_grid = []

for r in range(n) :
    for c in range(n) :
        if matrix[r][c] == 1 :
            count +=1
            bomb_grid.append([r,c])


maxi =  0

def bomb(answer,bomb_grid,count) :
    
    new_matrix = [[0]* n for _ in range(n)]
    pp = 0
    for t in range(count) :
        r,c =bomb_grid[t][0],bomb_grid[t][1]
        new_matrix[r][c] = 1
        a = answer[t]
        for i in range(n) :
            for j in range(n) :
                if a == 1:
                    if j == c and abs(i-r) <=2 :
                        new_matrix[i][j] =1

                elif a == 2 :
                    if abs(i-r) + abs(c-j) <= 1 :
                        new_matrix[i][j] = 1

                else :
                    if abs(i-r) == 1 and abs(j-c) == 1 :
                        new_matrix[i][j] = 1

    for i in range(n) :
        for j in range(n) :
            if new_matrix[i][j] == 1 :
                pp +=1


    return pp



def choose(num) :
    global maxi
    if num == count  :
        result  = bomb(answer,bomb_grid,count)
        maxi = max(result,maxi)

        return

    for i in range(1,4) :
        answer.append(i)
        choose(num +1)
        answer.pop()
    

choose(0)
print(maxi)