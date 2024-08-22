import sys


grid=  [list(map(int , input().split())) for _ in range(4)]


direct = input()
# print(*grid)

# print([grid[0][i] for i in range(4)])
# merge 에서 방향정보가 나와야할듯함
def  merge(arr):
    length = len(arr)
    new_lst = []
    new_t = []
    i = 0
    if direct == 'R' or direct == 'D' :
        arr = arr[::-1]
    for a in arr :
        if a != 0 :
            new_t.append(a)
    arr = new_t
    print(arr)
    length = len(arr)
    # print(arr)
    while i < length-1 :
        if arr[i] == arr[i+1] :
            new_lst.append(2*arr[i])
            i +=2
        else :
            if arr[i] != 0 :
                new_lst.append(arr[i])
            i +=1
    if arr[length-2] != arr[length-1]  and arr[length-1]!= 0 :
        new_lst.append(arr[length-1])

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

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix





if direct == 'U' :
    one,two,three,four = [grid[i][0] for i in range(4)],[grid[i][1] for i in range(4)],[grid[i][2] for i in range(4)],[grid[i][3] for i in range(4)]
    # print("checking", one,two,three,four)
    one,two,three,four = merge(one),merge(two), merge(three),merge(four)
    

elif direct == 'L' :
    one,two,three,four = grid[0],grid[1],grid[2],grid[3]
    one,two,three,four = merge(one),merge(two), merge(three),merge(four)
    # one,two,three,four = one[::-1],two[::-1],three[::-1],four[::-1]
elif direct == 'R' :
    one,two,three,four = grid[0],grid[1],grid[2],grid[3]
    one,two,three,four = merge(one),merge(two), merge(three),merge(four)
    

else :
    one,two,three,four = [grid[i][0] for i in range(4)],[grid[i][1] for i in range(4)],[grid[i][2] for i in range(4)],[grid[i][3] for i in range(4)]
    one,two,three,four = merge(one),merge(two), merge(three),merge(four)

grid = [one,two,three,four]
# print(grid)
if direct == "U" or direct == "D" :
    grid = transpose(grid)
# 
for g in grid :
    print(*g)
    





# print(*grid)