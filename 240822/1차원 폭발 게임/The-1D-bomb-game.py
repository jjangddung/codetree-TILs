import sys

n,m = map(int, input().split())

count = 0

grid = [int(input()) for _ in range(n)]


# print(grid)

def finding(index,length) :
    count = 0
    for j in range(index,length) :
        if grid[j] == grid[index] :
            count +=1
        else :
            return count
    return count


new = 1

while new != 0 :
    new = 0
    i  = 0
    new_lst = []
    length = len(grid)
    while i < length :
        count = finding(i,length)
        if count < m :
            for t in range(count) :
                new_lst.append(grid[i])
        else :
            new +=1
        i += count
    grid = new_lst
    # print(grid)




print(len(grid))

if len(grid) == 0 :
    pass
else :
    for _ in grid :
        print(_)