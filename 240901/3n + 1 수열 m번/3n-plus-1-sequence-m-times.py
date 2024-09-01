m = int(input())


for _ in range(m) :
    v = int(input())
    count = 0

    while v != 1 :
        if v % 2 == 0 :
            v= v//2
        
        else :
            v = 3*v +1 
        count +=1
    
    print(count)