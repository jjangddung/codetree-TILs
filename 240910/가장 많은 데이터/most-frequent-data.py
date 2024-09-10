n = int(input())



d  = {}

for _ in range(n) :
    value = str(input())

    if value not in d :
        d[value] = 1
    
    else :
        d[value] +=1


index = max(d) # index를 반환함
print(d[index])