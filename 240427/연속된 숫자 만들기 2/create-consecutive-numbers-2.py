import sys

def clear(p,q,r) :
    if q-p ==1 and r-q == 1 :
        return 0
    elif r- q ==2 or q-p == 2 :
        return 1
    else :
        return 2

p,q,r = map(int, input().split())
print(clear(p,q,r))