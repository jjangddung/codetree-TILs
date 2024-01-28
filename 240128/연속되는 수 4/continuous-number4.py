import sys



input = sys.stdin.readline




n = int(input())



arr = []


for i in range(n) :
    k = int(input())
    arr.append(k)





maximum = 1


for i in range(1,n) :
    cnt = 1

    for j in range(i,n) :
        if arr[j] > arr[j-1] :
            cnt +=1
            if j == n-1 :
                maximum = max(cnt , maximum)

        
        else :
            maximum = max(cnt, maximum)
            break


print(maximum)