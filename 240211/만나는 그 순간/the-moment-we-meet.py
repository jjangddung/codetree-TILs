import sys



input = sys.stdin.readline



n,m = map(int, input().split())


A_x = [0]
B_x = [0]




for _ in range(n) :

    d_list = list(map(str, input().split()))
    direction = d_list[0]
    length = int(d_list[1])

    for _ in range(length) :
        if len(A_x) == 1 :
            q = A_x[0]
        else :
            q = A_x[-1]
        
        if direction == "R" :
            A_x.append(q+1)
        
        else :
            A_x.append(q-1)


for _ in range(m) :

    d_list = list(map(str, input().split()))
    direction = d_list[0]
    length = int(d_list[1])

    for _ in range(length) :
        if len(B_x) == 1 :
            q = B_x[0]
        else :
            q = B_x[-1]
        
        if direction == "R" :
            B_x.append(q+1)
        
        else :
            B_x.append(q-1)



total_length = len(B_x)

for i in range(1,total_length) :
    if A_x[i] == B_x[i] :
        print(i)
        break
    
    if i == total_length-1 :
        print(-1)