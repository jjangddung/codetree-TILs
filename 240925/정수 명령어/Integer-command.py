from sortedcontainers import SortedSet



t = int(input())


for i in range(t) :
    k = int(input())
    s = SortedSet()

    for _ in range(k) :
        
        order = list(map(str, input().split()))
        order, num = order[0] , int(order[1])

        if order == 'I' :
            s.add(num)
        
        else :
            if len(s) != 0 :
                if num == -1 :
                    s.remove(s[0])

                else :
                    if len(s) != 1 :
                        s.remove(s[-1])
        # print(s)

    
    if len(s) >= 1 :
        print(s[-1], s[0])
    
    
    else :
        print("EMPTY")