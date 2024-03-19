import sys

input = sys.stdin.readline


x_1,y_1,x_2,y_2 = map(int, input().split())
x_3,y_3,x_4,y_4 = map(int, input().split())

print((max(x_2,x_4)-min(x_1,x_3))*(max(y_2,y_4)-min(y_1,y_3)))