n,m = map(int, input().split())
lst = [0]
order_lst  = []
s = {}
# print(new_lst)
for i in range(1,n+1) :
    lst.append(i)
    s[i] = [i]
    
    
    
for i in range(m) :
    a,b = map(int,input().split())
    order_lst.append([a,b])



for t in range(3) :
    for order in order_lst :
        a,b = order[0], order[1]
        if  b  not in s[lst[a]] :
            s[lst[a]].append(b)
        if a not in s[lst[b]] :
            s[lst[b]].append(a) 
        # s[a].add(b)
        # s[b].add(a)
        lst[a], lst[b] = lst[b], lst[a] 


# print(s)
for t in s :
    print(len(s[t]))