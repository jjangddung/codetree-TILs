import sys
import copy

n,m = map(int,  input().split())


grid = [
    list(map(int, input().split()))
    for _ in range(n)
]



back_lst = []
ans_lst = []

def backtracking(num,cnt) :

    if cnt > m :
        return

    if num == n :
        if cnt == m :
            ans_lst.append(copy.deepcopy(back_lst))
            # print(*back_lst)

        return

    back_lst.append(num)
    backtracking(num+1,cnt+1)

    back_lst.pop()
    backtracking(num+1,cnt)

backtracking(0,0)

# print(ans_lst)

result = 0

for ans in ans_lst :
    p1,p2 = ans
    p1_x, p1_y = grid[p1]
    p2_x, p2_y = grid[p2]

    distance = (p1_x-p2_x)**2+ (p1_y-p2_y)**2
    result = max(distance,result)

print(result)