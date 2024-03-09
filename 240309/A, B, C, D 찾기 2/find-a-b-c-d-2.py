import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

arr.sort()

for i in range(1,41) :
    count = 0
    for j in range(1,41) :
        for k in range(1,41) :
            for l in range(1,41) :
                new_arr = [i,j,k,l,i+j,j+k,k+l,l+i,i+k,j+l,i+j+k,i+j+l,i+k+l,j+k+l,i+j+k+l]
                new_arr.sort()

                if arr == new_arr :
                    print(i,j,k,l)
                    count =1
                    break
            if count == 1 :
                break
        
        if count == 1 :
            break
    if count == 1 :
        break