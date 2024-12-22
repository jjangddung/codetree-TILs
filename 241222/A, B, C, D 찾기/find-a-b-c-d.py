import sys

input = sys.stdin.readline

num_list = list(map(int, input().split()))
num_list.sort()
last_value = num_list[-1]

a = num_list[0]
b = num_list[1]
c = num_list[2]

def function(last_value,num_list) :

    for d in range(c, last_value) :
        if a+b+c+d == last_value :
            print(a,b,c,d)
            return 
    return

function(last_value,num_list)

