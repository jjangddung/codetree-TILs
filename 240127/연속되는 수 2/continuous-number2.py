import sys

input = sys.stdin.readline


n = int(input())




arr =[]
for _  in range(n) :
    k = int(input())

    arr.append(k)


cnt_list = [] 
for i in range(n) :
    cnt = 0
    for j in range(i,n) :
        if arr[i] == arr[j] :
            cnt +=1 
        
        else :
            cnt_list.append(cnt)
            break


if len(cnt_list) == 0 :
    print(1)

else :
    print(max(cnt_list))