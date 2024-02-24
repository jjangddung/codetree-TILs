import sys

input = sys.stdin.readline


n = int(input())

first_arr = list(map(int, input().split()))

second_arr = list(map(int, input().split()))



def first_case(arr) :
    for i in range(3) :
        if 2< abs(first_arr[i]- new_arr[i]) < n-2  :
            return False
            break
    return True

def second_case(arr) :
    for i in range(3) :
        if 2 < abs(second_arr[i]- new_arr[i]) <n-2  :
            return False
            break
    return True


count = 0

for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1,n+1) :
            new_arr = [i,j,k]
            if first_case(new_arr) == True or second_case(new_arr) == True :
                count +=1

print(count)