import sys

n = int(input())

check_lst = [
    list(map(int, input().split()))
    for _ in range(n)
]



mini = sys.maxsize

for i in range(1,n-1) :
    distance= 0
    prev_x, prev_y = check_lst[0][0], check_lst[0][1]
    for j in range(n) :
        if i == j :
            continue
        present_x,present_y = check_lst[j][0], check_lst[j][1]

        distance += (abs(present_x-prev_x) + abs(present_y -prev_y))
        prev_x,prev_y = present_x,present_y
    
    mini = min(distance,mini)
        
        
print(mini)