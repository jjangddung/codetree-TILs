import sys

input = sys.stdin.readline


n = int(input())

num_sum_list = list(map(int, input().split()))


for i in range(1,n) :
    count = 0
    new_list = []

    new_list.append(i)

    for num in range(n-1) :
        if len(new_list) == 1 :
            last = new_list[0]
        else :
            last = new_list[-1]
        if last <= 0 :
            count +=1
            break

        new_list.append(num_sum_list[num]-last)
    set_new_list = set(new_list)
    if count == 0 and len(set_new_list) == n :
        for p in new_list :
            print(p, end= " ")
    # new_list.append(num_sum_list[-1]-last)