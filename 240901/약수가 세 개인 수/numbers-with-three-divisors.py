start, end=  map(int, input().split())

count = 0
for num in range(start,end+1) :
    lst = []
    for v in range(1,num//2+1) :
        if num % v == 0 :
            lst.append(v)
            lst.append(num//v)
    
    lst = set(lst)
    length = len(lst)
    if length == 3 :
        count +=1

print(count)