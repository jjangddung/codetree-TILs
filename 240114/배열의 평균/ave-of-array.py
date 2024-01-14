import sys


input = sys.stdin.readline

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))


sum_1 = sum(list_1)

sum_2 = sum(list_2)

print(sum_1/len(list_1), sum_2/len(list_2))


list_3 = []
for i in range(4) :
    sum_3 = 0 
    sum_3 = list_1[i] + list_2[i]

    list_3.append(sum_3/2)

for k in list_3 :
    print(k, end= " ")


print()
print((sum_1+sum_2)/8)