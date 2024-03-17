import sys

input = sys.stdin.readline

sum_list = list(map(int, input().split()))
sum_list.sort()
max_sum = max(sum_list)
for a in range(max_sum) :
    for b in range(a,max_sum) :
        for c in range(b,max_sum) :
            new_list = [a,b,c,a+b,a+c,b+c,a+b+c]
            new_list.sort()
            if new_list == sum_list :
                print(a,b,c)
                break