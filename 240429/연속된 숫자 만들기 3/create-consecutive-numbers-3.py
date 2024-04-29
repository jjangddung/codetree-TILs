import sys


input  = sys.stdin.readline



a,b,c = map(int, input().split())

length_1 = b -a
length_2 = c -b
if length_1  == 1 and length_2 == 1 :
    print(0)
else :
    print(max(length_1,length_2)-1)