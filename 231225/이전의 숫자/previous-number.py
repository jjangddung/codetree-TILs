import sys;

input = sys.stdin.readline 

n = int(input())

k_list = []

k_list = list(map(int, input().split()))


ans_list = []

for  j in k_list :
    if j == 0 :
        break
    ans_list.append(j)


ans_list = ans_list[::-1]

sum = 0

for i in range(5) :
    sum += ans_list[i]


print(sum)