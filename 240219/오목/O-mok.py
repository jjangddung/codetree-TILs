import sys

input = sys.stdin.readline


arr = [list(map(int, input().split())) for _ in range(19)]

def straight(arr, i,j) :
    standard = arr[i][j]

    if standard == 0 :
        return False
    
    else :

        for k in range(-2,3) :
            if arr[i][j+k] != standard :
                return False
                break
        return True


def up_down(arr,i,j) :
    standard = arr[i][j]
    if standard == 0 :
        return False
    
    else :

        for k in range(-2,3) :
            if arr[i+k][j] != standard :
                return False
                break

        return True 


def diagonal_1(arr,i,j) :
    standard = arr[i][j]

    if standard == 0 :
        return False

    else :

        for k in range(-2,3) :
            if arr[i+k][j+k] != standard :
                return False
                break
        return True
def diagonal_2(arr,i,j) :
    standard = arr[i][j]

    if standard == 0 :
        return False
    else :

        for k in range(-2,3) :
            if arr[i+k][j-(k)] != standard :
                return False
                break
        return True


grade = 0

for i in range(2,17) :
    for j in range(2,17) :
        if straight(arr,i,j) == True or up_down(arr,i,j) == True or diagonal_1(arr,i,j) == True or diagonal_2(arr,i,j) == True :
            print(arr[i][j])
            print(i+1 , j+1)

            grade +=1
            break


if grade == 0 :
    print(0)