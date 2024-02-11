import sys

input = sys.stdin.readline


n = int(input())




n_list = [int(input()) for _ in range(n)]



length = 0
maximum = 0
value =  False

def checking(t) :
    if t < 0 :
        return False
    
    else :
        return True

        

for i in range(n) :
    length = 0

    if n_list[i] < 0 :
        value = False
    else :

        value = True

    

    for j in range(i,n) :
        k = n_list[j]

        if checking(k) == value :
            length +=1
            if j == n-1 :
                maximum = max(maximum,length)
        

        else :
            maximum = max(maximum,length)
            break

print(maximum)