n = int(input())


matrix = list(map(int, input().split()))


# pivot 값을 정하고 그 값을 기준으로  나눠야한다.
# 데이터가 3개 이하면 피벗은 반드시 마지막 값이 됨
# 데이터가 4개 이상이면 맨 왼쪽, 오른쪽, 가운데 (나머지 버림) 값 중 중간 값을 선택함
# 피벗이 선택되면 먼저 구간의 맨 끝 원소와 꼭 교환해야함


def quick_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    pivot = arr[-1]
    new_arr1 = []
    new_arr2 = []
    for i in range(len(arr)-1) :
        if arr[i] < pivot :
            new_arr1.append(arr[i])
        else :
            new_arr2.append(arr[i])
    

    return quick_sort(new_arr1) + [pivot] + quick_sort(new_arr2)


print(*quick_sort(matrix))