n = int(input())



d = {}

for _ in range(n) :
    order = list(map(str, input().split()))
    
    if order[0] == 'add' :
        d[order[1]] = int(order[2])

    
    elif order[0] == 'find' :
        if order[1] not in d :
            print('None')
        
        else :
            print(d[order[1]])
    
    else:
        d.pop(order[1])