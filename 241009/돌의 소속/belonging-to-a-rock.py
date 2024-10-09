import sys


n,q = map(int, input().split())


ston_lst = [0]*(n+1)

one_lst = [0]*(n+1)
two_lst = [0]*(n+1)
three_lst = [0]*(n+1)



for i in range(1,n+1) :
    num = int(input())
    ston_lst.append(num)

    one_lst[i] = one_lst[i-1]
    two_lst[i] = two_lst[i-1]
    three_lst[i] = three_lst[i-1]

    if num == 1 :
        one_lst[i] +=1

    elif num == 2: 
        two_lst[i] +=1

    else :
        three_lst[i] +=1    


for _ in range(q) :
    s,e = map(int, input().split())
    one,two,three= 0,0,0

    one = one_lst[e] - one_lst[s-1]
    two = two_lst[e] - two_lst[s-1]
    three = three_lst[e] - three_lst[s-1] 
    print(one,two,three)