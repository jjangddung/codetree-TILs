import sys

input = sys.stdin.readline

n= int(input())


point_arr = [list(map(int, input().split())) for _ in range(n)]


point_arr.sort()
count = 0


for i in range(11) :
    for j in range(11) :

        
        new_list  = []

        for element in point_arr :
            if i == element[0] :
                new_list.append(element)
        
        for element in point_arr :
            if j == element[1] :
                new_list.append(element)

        if len(new_list) != 0 : 
            tuple_list = [tuple(inner_list) for inner_list in new_list]
            new_set = set(tuple_list)
            new_list = list(new_set)
            new_list.sort()
        
        else :
            break

 
        for k in range(11):

            ori_list_1 = new_list.copy()
            ori_list_2 = new_list.copy()

            for element in point_arr :
                if k == element[0] :
                    ori_list_1.append(element)
            
            tuple_list = [tuple(inner_list) for inner_list in ori_list_1]
            new_set = set(tuple_list)
            ori_list_1 = set(new_set)
            ori_list_1 = list(ori_list_1)
            ori_list_1.sort()
            
            for element in point_arr :
                if k == element[1] :
                    ori_list_2.append(element)

            tuple_list = [tuple(inner_list) for inner_list in ori_list_2]
            ori_list_2 = set(tuple_list)
            ori_list_2 = list(ori_list_2)
            ori_list_2.sort()

            if len(ori_list_1) == len(point_arr) or len(ori_list_2) == len(point_arr) :
                count +=1
                break


if count == 0 :
    print(0)

else :
    print(1)