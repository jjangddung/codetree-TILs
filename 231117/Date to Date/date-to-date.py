import sys

input = sys.stdin.readline


a,b,c,d = map(int, input().split())



sum_1 = 0
sum_2 = 0
for i in range(1,a) :
    if i <= 7 :
        if i % 2 != 0 :
            sum_1 += 31
        else :
            if i == 2 :
                sum_1 += 28
            else :
                sum_1 += 30
    else :
        if i % 2 == 0 :
            sum_1 += 31
        else :
            sum_1 += 30


sum_1 += b

for i in range(1,c) :
    if i <= 7 :
        if i % 2 != 0 :
            sum_2 += 31
        else :
            if i == 2 :
                sum_2 += 28
            else :
                sum_2 += 30
    else :
        if i % 2 == 0 :
            sum_2 += 31
        else :
            sum_2 += 30

sum_2 += d

print(sum_2-sum_1+1)