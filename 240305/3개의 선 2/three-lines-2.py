import sys

input = sys.stdin.readline

n= int(input())


point_arr = [list(map(int, input().split())) for _ in range(n)]


point_arr.sort()
count = 0

new_list = [1,2,3,4]
ori_list = [5,6,7,8]




def checking_x(num) :
    new_list = []

    for element in point_arr :
        if num == element[0] :
            new_list.append(element)
    
    return new_list


def checking_y(num) :
    new_list = []

    for element in point_arr :
        if num == element[1] :
            new_list.append(element)
    
    return new_list






for i in range(11) :

    for j in range(11) :

        for k in range(11) :
            
            for x in range(2) :
                for y in range(2) :
                    for z in range(2) :
                        if x == 0 :
                            new_list_1 = checking_x(i)
                        else :
                            new_list_1 = checking_y(i)
                        
                        if y == 0 :
                            new_list_2 = checking_x(j)
                        
                        else :
                            new_list_2 = checking_y(j)
                        
                        if z == 0 :
                            new_list_3 = checking_x(k)
                        else :
                            new_list_3 = checking_y(k)
                        standard = new_list_1 + new_list_2 +new_list_3

                        tuple_list = [tuple(inner_list) for inner_list in standard]
                        new_set = set(tuple_list)
                        standard = list(new_set)

                        standard.sort()

                        if len(standard) == n :
                            count +=1



if count == 0 :
    print(0)

else :
    print(1)