start,end = map(int, input().split())

count = 0

for num in range(start, end +1) :
    lst = []

    for t in range(2,num//2+1) :
        if num % t == 0 :
            lst.append(t)
            if t != (num//t) :
                lst.append(num//t)
    lst = set(lst)
    lst = list(lst)
    # print(num,lst)
    if sum(lst)+1 == num :
        count +=1


print(count)