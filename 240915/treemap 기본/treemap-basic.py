from sortedcontainers import SortedDict

sd = SortedDict()

n = int(input())


for _ in range(n) :
    order = list(map(str, input().split()))

    if len(order) ==  3 :
        key, value = int(order[1]), int(order[2])
        sd[key] = value

    elif len(order) == 2:
        if order[0] == "remove" :
            sd.pop(int(order[1]))
        
        else :
            if int(order[1]) in sd :
                print(sd[int(order[1])])
            
            else :
                print("None")
    
    else :
        # sd = sorted(sd)
        if len(sd) == 0 :
            print("None")
        for s in sd :
            print(sd[s], end= " ")
        print()