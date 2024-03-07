import sys

input = sys.stdin.readline


n = int(input())


arr = [list(map(int,input().split())) for _ in range(n)]


k_list = []

if n == 1 :
    print(arr[0][0])
else :

    for i in range(1, 10001) :
        result = 2*i
        count = 0
        for element in arr :
            if element[0] <= result <= element[1] :
                result *=2
                
                pass
            else :
                count +=1
                break
        if count == 0 :
            print(i)
            break
        

# print(k_list)