import sys

input = sys.stdin.readline


distance = int(input())



for time in range(1,1000000) :
    if time % 2 == 0 :
        V_max = time//2
    else :
        V_max = time //2 +1

    V_list = []
    for v in range(1,V_max) :
        V_list.append(v)
        V_list.append(v)
    V_list.append(V_max)
    sorted_V_list = sorted(V_list)

    # print(V_list)
    minus = distance- sum(V_list) 
    if minus == 0 :
        print(time)
        break

    if minus in sorted_V_list :
        print(time +1)
        break