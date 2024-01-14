import sys

input = sys.stdin.readline


n,m = map(int, input().split())

cnt = 0 


list_2 = []


for i in range(m) :
    list_1 = []
    for j in range(1,n+1) :
        list_1.append(cnt)
        cnt+=1;
    if i %2 != 0 :
        list_2.append(list_1[::-1])
    else :
        list_2.append(list_1)


for i in range(n) :
    for j in range(m) :
        print(list_2[j][i], end = " ")
    print()