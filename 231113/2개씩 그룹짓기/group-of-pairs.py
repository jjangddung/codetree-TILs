import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))

num_list.sort()
rev_list = num_list[::-1]



r_list = []

for i in range(N) :
    q_list = []
    q_list.append(num_list[i])
    q_list.append(rev_list[i])
    result = sum(q_list)
    r_list.append(result)


print(max(r_list))