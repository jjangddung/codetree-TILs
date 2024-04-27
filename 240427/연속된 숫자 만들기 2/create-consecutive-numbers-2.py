import sys

def clear(p,q,r) :
    if r- q ==1 or q-p == 1 :
        return 1
    else :
        return 2

p,q,r = map(int, input().split())
print(clear(p,q,r))