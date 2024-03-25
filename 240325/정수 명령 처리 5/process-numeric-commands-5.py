import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    
    put = input().split()
    
    if len(put) == 1 :
        order = put[0]
    else :
        order = put[0]
        num = int(put[1])
    

    if order == "push_back" :
        arr.append(num)
    elif order == "pop_back" :
        arr.pop()
    elif order == "size" :
        print(len(arr))
    else :
        print(arr[num-1])