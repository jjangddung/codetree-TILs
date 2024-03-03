import sys

input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split()))

mini  = 100000000

for i in range(n) :
    for j in range(n) :
        new_list = []

        for p in range(n) :
            ele = arr[p]

            if p == i :
                ele = 2 * arr[p]
            if p == j :
                continue
            new_list.append(ele)
        # print(new_list)
        total_minus = 0
        for k in range(n-2) :
            total_minus += abs(new_list[k+1] - new_list[k])
        mini = min(total_minus,mini)


print(mini)