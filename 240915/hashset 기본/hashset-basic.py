n  = int(input())


s = set()

for _ in range(n) :
    order= list(map(str,input().split()))
    # print(order)
    value = int(order[1])


    if order[0] == "add" :
        s.add(value)
    
    elif order[0] == "find" :
        if  value in s :
            print('true')
        else :
            print('false')
    
    else :
        s.remove(value)