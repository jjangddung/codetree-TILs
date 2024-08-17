import sys

alpha = input()

length = len(alpha)

def move(string,num) :
    new_str = string[num:]+string[:num]

    return new_str

def counting(string) :
    length = len(string)
    depth = []
    n = 1

    for t in range(1,length) :
        if string[t] == string[t-1] :
            n +=1


        else :
            depth.append(n)
            n =1
    depth.append(n)
        

    dep = len(depth)
    count = 0

    for p in range(dep) :
        if depth[p] < 10 :
            count +=2
        else :
            count +=3
    # print(new_str,count)
    return count




maxi = sys.maxsize

for i in range(1,length) :
    new_str = move(alpha,i)
    num = counting(new_str)
    maxi = min(num, maxi)

print(maxi)