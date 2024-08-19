#끝 점 좌표 4개를 임의로 정하기


import sys

input = sys.stdin.readline


n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def change_grid(value,n,m) :
    new_value = [value//m,value % m]

    return new_value

def width_height(value_1,value_2) :
    width = value_2[0] - value_1[0] +1
    height = value_2[1] - value_1[1] +1

    return [width,height]

maxi  = -99999999999999999999999999999999999999

for x_1,y_1 in zip (range(n), range(m)) :
    for x_2, y_2 in zip(range(x_1,n), range(y_1, m)) :
        for x_3,y_3 in zip (range(n), range(m)) :
            for x_4, y_4 in zip(range(x_3,n), range(y_3, m)) :
                new_matrix = [[0]*m  for _ in range(n)]
                total = 0
                count = 0

                for p in range(x_1,x_2+1) :
                    for q in range(y_1,y_2+1) :
                        new_matrix[p][q] += 1

                for p in range(x_3,x_4+1) :
                    for q in range(y_3,y_4+1) :
                        if new_matrix[p][q] != 0 :
                            count +=1
                        new_matrix[p][q] += 1
                
                if count != 0 :
                    continue

                for t in range(n) :
                    for w in range(m) :
                        if new_matrix[t][w] == 1 :
                            total += matrix[t][w]

                maxi = max(maxi,total)

print(maxi)