import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

p_list = []
q_list = []


for i in range(N) :
    if i % 2 == 0 :
        p_list.append(num_list[i])
        if len(p_list) != N :
            p_list.append(num_list[2*N-1-i])
    else :
        q_list.append(num_list[i])
        if len(q_list) != N :
            q_list.append(num_list[2*N-1-i])

result =max(sum(p_list),sum(q_list))
print(result)