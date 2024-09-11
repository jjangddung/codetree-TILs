import sys

a,b,c,d ={},{},{},{}

n = int(input())
for i in range(4) :
    lst = list(map(int, input().split()))
    
    if i == 0:
        for l in lst :
            if l not in a :
                a[l] = 1

            else :
                a[l] += 1
    
    elif i == 1:
        for l in lst :
            if l not in b :
                b[l] = 1


            else :
                b[l] += 1

    elif i == 2:
        for l in lst :
            if l not in c :
                c[l] = 1


            else :
                c[l] += 1
    
    else:
        for l in lst :
            if l not in d :
                d[l] = 1


            else :
                d[l] += 1

count = 0
for q in a :
    for w in b :
        for e in  c :
            for r in d :
                if q + w+ e+ r != 0 :
                    continue
                count += 1
                # print(q,w,e,r)

print(count)