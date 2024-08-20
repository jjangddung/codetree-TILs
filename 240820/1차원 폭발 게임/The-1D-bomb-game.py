import sys


n,m = map(int , input().split())

grid = [int(input()) for _ in range(n)]



def array(new_grid) :
    new_lst = []
    count  = 0
    for g in new_grid :

        if g[1] >= m :
            count +=1
            continue

        for t in range(g[1]) :
            new_lst.append(g[0])

    # print(new_lst,count)

    return [new_lst,count]

def group(grid) :
    new_list = []
    length = len(grid)

    if length == 1 :
        return [[grid[0]],1]

    count  = 1
    num = 0

    for i in range(length-1) :
        if grid[i] == grid[i+1] :
            count +=1

            
        
        else :
            num = grid[i]
            new_list.append([num,count])
            count = 1
    num = grid[-1]
    new_list.append([num,count])

    ans = array(new_list)
    new_lst = ans[0]
    grid = new_lst
    answer = ans[1]


    return  ans

answer = group(grid)
# print(answer[0])

if m == 1 :
    print(0)
else :
    while  answer[1] != 0 :
        # print("list: ", answer[0])
        answer = group(answer[0])


    # print("answer: ", answer)

    result = answer[0]
    print(len(result))
    for _ in result :
        print(_)