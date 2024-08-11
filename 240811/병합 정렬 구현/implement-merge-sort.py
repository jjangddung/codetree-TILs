n = int(input())

matrix = list(map(int, input().split()))

# 리스트들을 반으로 나누는 것부터 해보자!


div_list = []


def func(arr) :
    length  = len(arr)
    if length == 1 :
        div_list.append(arr)
        return 

    mid = int(length/2)
    new_list_1 = arr[:mid]
    func(new_list_1)
    new_list_2 = arr[mid:]
    func(new_list_2)


func(matrix)
#print(div_list)

# 나눴으면 합쳐보자 합치는 방식은...?

def merge(arr1, arr2) :
    new_merge = []

    new_len = len(arr1) + len(arr2)
    k = 0
    i ,j = 0,0

    while k  == n :
        if arr1[i] <= arr2[j] :
            new_merge[k] = arr1[i]
            k+=1, i +=1
        else :
            new_merge[k] = arr2[j]
            k+=1, j +=1