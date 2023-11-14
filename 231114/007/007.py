import sys


input = sys.stdin.readline


c, p , t = map(str, input().split())



class Codetree  :
    def __init__(self, code, point , time) :
        self.c = code
        self.p = point
        self.t = time


codetree = Codetree(c,p,t)

print(f'secret code : {codetree.c}')
print(f'meeting point : {codetree.p}')
print(f'time : {codetree.t}')