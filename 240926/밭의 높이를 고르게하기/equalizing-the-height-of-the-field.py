import sys

n,h,t = map(int, input().split())

grid = list(map(int, input().split()))



cost_lst = []


for g in grid :
    cost_lst.append(abs(g-h))

# print(cost_lst)


mini_cost = sys.maxsize

for i in range(n-t+1) :
    new_lst = cost_lst[i:i+t]
    cost = sum(new_lst)
    mini_cost = min(cost,mini_cost)

print(mini_cost)