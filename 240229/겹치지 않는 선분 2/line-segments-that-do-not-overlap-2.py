import sys

input = sys.stdin.readline


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

# print(arr-)




count = 0

def check_cross(num) :

    some = 0



    a_1 =arr[num][0]
    a_2 = arr[num][1]
    a_chai = a_2 - a_1


    for p in range(n) :
        if p == num :
            continue

        b_1, b_2 = arr[p][0] , arr[p][1]

        b_chai = b_2 - b_1

        up = a_1*b_chai - b_1*a_chai
        down = b_chai-a_chai

            
        if down != 0 :
            result = up/down
            

            if a_1<= result <= a_2 and b_1 <= result <= b_2 :
                
                some +=1
        
    if some == 0 :
        return True
    else :
        return False






for i in range(n) :
    if check_cross(i) :
        # print(i)
        count +=1

print(count)