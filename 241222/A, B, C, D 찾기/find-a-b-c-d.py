import sys

input = sys.stdin.readline

num_list = list(map(int, input().split()))
num_list.sort()
last_value = num_list[-1]


def function(last_value,num_list) :

    for a in range(1,last_value) :
        for b in range(a, last_value) :
            for c in range(b, last_value) :
                for d in range(c, last_value) :
                    new_list = []
                    new_list = [a,b,c,d,a+b,b+c,c+d,d+a,a+c,b+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d]
                    new_list.sort()
                    if new_list == num_list :
                        print(a,b,c,d)
                        return
    return

function(last_value,num_list)

