import sys

input = sys.stdin.readline


t,a,b = map(int,  input().split())

arr  = [0]* 1001
S_list,N_list = [],[]

count = 0

for _ in range(t) :
    
    alpha, num = map(str, input().split())
    num = int(num)
    arr[num] = alpha
    if alpha == "S" :
        S_list.append(num)
    else :
        N_list.append(num)
S_list.sort()
N_list.sort()
# print(S_list)
# print(N_list)

for i in range(a,b+1) :
    s_mini = 100000
    n_mini = 100000


    for j in range(len(S_list)) :
        # print(S_list[j])
        mini = abs(S_list[j]-i)
        # print("mini:",mini)
        s_mini = min(mini,s_mini)
    for k in range(len(N_list)) :
        mini = abs(N_list[k]-i)
        n_mini = min(mini,n_mini)
    if s_mini <= n_mini :
        # print(i)
        count +=1

print(count)