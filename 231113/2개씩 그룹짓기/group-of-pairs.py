import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

a_list= []
b_list= []

a_list.append(num_list[0])
b_list.append(num_list[1])

for i in range(2,2*N) :
    if sum(a_list) > sum(b_list) :
        a_list.append(i)
    else :
        b_list.append(i)

print(max(sum(a_list),sum(b_list)))