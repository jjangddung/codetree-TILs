n = int(input())



for num in range(1,n+1) :
    lst = []
    count = 1
    if num == 1 :
        continue

    for v in range(1,num//2+1) :
        if num % v == 0 :
            if v != 1 :
                count = 0
                break
    if count == 1 :
        print(num, end= " ")