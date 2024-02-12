import sys

input = sys.stdin.readline


n, m = map(int, input().split())


# >>> 위치 차이만큼 잡기.
a_arr = [list(map(str, input().split())) for _ in range(n)]

b_arr = [list(map(str, input().split())) for _ in range(m)]


a_list = [0] 

b_list = [0] 

for arr in a_arr :
    direct = arr[1]
    length  = int(arr[0])

    


    for j in range(length) :

        if len(a_list) == 1 :
            q  = a_list[0]

        else :
            q = a_list[-1]

        if direct == 'R' :
            a_list.append(q+1)
        
        else :
            a_list.append(q-1)

# print(a_list)

for arr in b_arr :
    direct = arr[1]
    length  = int(arr[0])

    


    for j in range(length) :

        if len(a_list) == 1 :
            q  = b_list[0]

        else :
            q = b_list[-1]

        if direct == 'R' :
            b_list.append(q+1)
        
        else :
            b_list.append(q-1)


# print(b_list)


real_chai = len(b_list) - len(a_list)

if real_chai > 0 :
    for i in range(real_chai) :
        q = a_list[-1]

        a_list.append(q)

else :
    for j in range(abs(real_chai)) :
        q = b_list[-1]

        b_list.append(q)




result_list = []

for i in range(len(b_list)) :
    result = a_list[i] - b_list[i]
    result_list.append(result)



# print(result_list)
count = 0

for i in range(1, len(b_list)) :
    if result_list[i] != result_list[i-1] and result_list[i] == 0 :
        count +=1


print(count)