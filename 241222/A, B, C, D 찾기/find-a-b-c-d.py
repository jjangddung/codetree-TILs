import sys

input = sys.stdin.readline

num_list = list(map(int, input().split()))
num_list.sort()
last_value = num_list[-1]

a = num_list[0]
b = num_list[1]
c = num_list[2]

def function(last_value,num_list) :
    d = last_value - a-b-c

    print(a,b,c,d)
    return

function(last_value,num_list)

