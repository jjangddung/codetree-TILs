import sys

n = int(input())



d  = {}
maximum = -sys.maxsize
for _ in range(n) :
    value = str(input())

    if value not in d :
        d[value] = 1
    
    else :
        d[value] +=1

    maximum = max(maximum,d[value])

# index = max(d) # index를 반환함
# print(d[index])
print(maximum)