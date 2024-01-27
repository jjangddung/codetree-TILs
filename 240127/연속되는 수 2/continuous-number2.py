import sys

input = sys.stdin.readline


n = int(input())




arr =[]
for _  in range(n) :
    k = int(input())

    arr.append(k)


cnt_list = [] 
maximum = 1
for i in range(n) :
    cnt = 0
    for j in range(i,n) :
        if arr[i] == arr[j] :
            cnt +=1 
        
        else :
            maximum = max(cnt,maximum)
            break

print(maximum)