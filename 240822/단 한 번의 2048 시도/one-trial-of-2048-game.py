import sys


grid=  [list(map(int , input().split())) for _ in range(4)]


direct = input()
# print(*grid)

# print([grid[0][i] for i in range(4)])
# merge 에서 방향정보가 나와야할듯함
def  merge(arr):
    length = len(arr)
    new_lst = []
    i = 0
    if direct == 'R' or direct == 'D' :
        arr = arr[::-1]
    
    # print(arr)
    while i < length-1 :
        if arr[i] == arr[i+1] :
            new_lst.append(2*arr[i])
            i +=2
        else :
            if arr[i] != 0 :
                new_lst.append(arr[i])
            i +=1
    if arr[-1] != 0 :
        new_lst.append(arr[-1])

    if direct == 'R' or  direct == 'D' :
        new_lst = new_lst[::-1]
    # print(new_lst)
    # print(direct)
    new_lst = plus_zero(direct,new_lst)

    return new_lst

def plus_zero(direct,new_lst) :
    # print(direct)
    something = [0] * (4-len(new_lst))
    if direct == 'L' or direct ==  'U'  :
        new_lst = new_lst + something
        # print(direct)
    else:
        new_lst = something + new_lst
        
        # print(direct)
    return new_lst

def change(matrix) :
    for i in range(4) :
        for j in range(4) :
            matrix[i][j] = matrix[j][i]
    
    return matrix




if direct == 'U' :
    one,two,three,four = [grid[0][i] for i in range(4)],[grid[1][i] for i in range(4)],[grid[2][i] for i in range(4)],[grid[3][i] for i in range(4)]
    

elif direct == 'L' :
    one,two,three,four = grid[0],grid[1],grid[2],grid[3]
    one,two,three,four = merge(one),merge(two), merge(three),merge(four)
    # one,two,three,four = one[::-1],two[::-1],three[::-1],four[::-1]
elif direct == 'R' :
    one,two,three,four = grid[0],grid[1],grid[2],grid[3]
    one,two,three,four = merge(one),merge(two), merge(three),merge(four)
    

else :
    one,two,three,four = [grid[0][i] for i in range(4)],[grid[1][i] for i in range(4)],[grid[2][i] for i in range(4)],[grid[3][i] for i in range(4)]

grid = [one,two,three,four]
if direct == "U" or direct == "D" :
    grid = change(grid)

for g in grid :
    print(*g)
    





# print(*grid)