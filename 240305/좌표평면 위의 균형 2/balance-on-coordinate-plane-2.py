import sys

input = sys.stdin.readline

n = int(input())


point_arr = [list(map(int, input().split())) for _ in range(n)]

def quadrant(x,y,ele) :
    if ele[0] > x and ele[1] > y  :
        return 1
    elif ele[0] < x and ele[1] > y :
        return 2
    
    elif ele[0] < x and ele[1] < y :
        return 3

    
    elif ele[0] > x and ele[1] > y :
        return 4


result_list = []
maxi = 10000

for i in range(1,101) :
    for j in range(1,101) :
        if i % 2 != 0 or j % 2 != 0 :
            continue
        # print(i,j)
        first = 0
        second = 0
        third = 0    
        forth = 0

        # for element in point_arr :
            # if checking(i,j,element) == False :
                # break
        for element in point_arr :
            result = quadrant(i,j,element)
            if result == 1:
                first +=1
            elif result == 2:
                second +=1
            elif result == 3:
                third +=1
            else :
                forth +=1
        mid = max(first,second,third,forth) - min(first,second,third,forth)

        if mid < maxi :
            result_list = [first,second,third,forth]
            maxi = mid

print(max(result_list))