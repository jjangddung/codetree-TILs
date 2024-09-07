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

result = sys.maxsize

for ans in ans_lst :
    length = len(ans)
    semi = 0

    for i in range(length) :
        for j in range(i, length) :
            p1  = grid[i]
            p2 =  grid[j]
            distance = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
            semi = max(distance,semi)
    result = min(semi,result)
            

print(result)