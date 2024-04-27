import sys

def clear(p,q,r) :
    if r- q ==2 or q-p == 2 :
        return 1
    else :
        return 2

p,q,r = map(int, input().split())
print(clear(p,q,r))