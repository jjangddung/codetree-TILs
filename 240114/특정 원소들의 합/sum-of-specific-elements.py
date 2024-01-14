import sys

input = sys.stdin.readline



list_1 = []
list_2= []

for i in range(4) :
    list_1 = list(map(int, input().split()))

    list_2.append(list_1)

result = 0

for i in range(4) :
    for j in range(i+1) :
        result += list_2[i][j]
    


print(result)