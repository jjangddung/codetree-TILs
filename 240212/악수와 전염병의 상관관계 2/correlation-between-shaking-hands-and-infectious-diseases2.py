import sys


input = sys.stdin.readline

n,k,p,T = map(int, input().split())


time_list =[list(map(int, input().split())) for _ in range(T)]

n_list = [0 for _ in range(n+1)]

n_list[p] = 1

k_list = [k for _ in range(n+1)]

# print(k_list)


time_list.sort()

# print(time_list)
for people in time_list :
    # t = people[0]
    x = people[1]
    y = people[2]

    if n_list[x] == 1 and n_list[y]  == 0 :
        if k_list[x] >= 1 :
            k_list[x] -=1
            n_list[y] = 1
    
    elif n_list[x] == 1 and n_list[y] == 1:
        if k_list[x] >= 1  :
            k_list[x] -= 1
        
        if k_list[y] >= 1 :
            k_list[y] -= 1
    
    elif n_list[x] == 0 and n_list[y] == 1 :
        if k_list[y] >= 1 :
            k_list[y] -= 1
            n_list[x] = 1

for i in range(1,n+1) :
    print(n_list[i], end= "")