import sys


alpha = str(input())


d = {}

for i in range(len(alpha)) :
    if alpha[i] not in d :
        d[alpha[i]] = 1
    
    else :
        d[alpha[i]] +=1
    

total = []

for v in d :
    if d[v] == 1:
        total.append(v)

if len(total) != 0 :
    print(total[0], sep = " ")

else :
    print("None")