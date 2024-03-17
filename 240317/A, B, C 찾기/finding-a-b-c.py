import sys

input = sys.stdin.readline

sum_list = list(map(int, input().split()))
sum_list.sort()
max_sum = max(sum_list)
min_value = min(sum_list) 
for a in range(7) :
    for b in range(a+1,7) :
        for c in range(b+1,7) :
            A,B,C = sum_list[a],sum_list[b],sum_list[c]
            new_list = [A,B,C,A+B,A+C,B+C,A+B+C]
            new_list.sort()
            if new_list == sum_list :
                print(A,B,C)
                break