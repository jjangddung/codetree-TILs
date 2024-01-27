import sys

input = sys.stdin.readline


n = int(input())




arr =[]
for _  in range(n) :
    k = int(input())

    arr.append(k)


cnt_list = []


for i in range(n) :
    s = arr[i]
    cnt = 0
    if  s < 0 :
        s = -1
    else :
        s = 1
   
    for j in range(i,n) :
        if arr[j] != abs(arr[j]) :
            if s == -1 :
                cnt +=1
                if j == n :
                    cnt_list.append(cnt)
                    
            else :
                cnt_list.append(cnt)
                break
        
        else :
            if s != -1 :
                cnt +=1
                if j  == n  :
                    cnt_list.append(cnt)
            
            else :
                cnt_list.append(cnt)
                break


if len(cnt_list) == 0 :
    print(1)

else :
    print(max(cnt_list))