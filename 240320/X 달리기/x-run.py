import sys

input = sys.stdin.readline


distance = int(input())





for time in range(1,1000000) :
    if time % 2 == 0 : #최대속도 정의하기
        V_max = time//2
    else :
        V_max = time //2 +1

    V_list = []
    result = 0

    for v in range(1,V_max) :
        V_list.append(v)
        result += 2*v
    V_list.append(V_max)

    
    minus = distance- result
    if minus in V_list  :
        print(time)
        break
    else :
        result += V_max
        V_list.append(V_max)
        # print(V_list)
        minus -= V_max
        if minus in V_list :
            print(time+1)
            break