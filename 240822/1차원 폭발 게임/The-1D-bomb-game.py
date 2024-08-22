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
    for i in range(n) :
        length = len(grid)
        count = finding(i,length)
        if count >= m:
            grid = grid[:i] + grid[i+count:]
            # print(grid)
            new+=1
            break


print(len(grid))

if len(grid) == 0 :
    pass
else :
    for _ in grid :
        print(_)