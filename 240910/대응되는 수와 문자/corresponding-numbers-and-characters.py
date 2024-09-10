import sys


n,m = map(int, input().split())


d = {}

for i in range(n) :
    value = str(input())
    string = i + 1
    string = str(string)
    
    d[value] = string
    d[string] = value


for _ in range(m) :
    v = str(input())


    print(d[v])