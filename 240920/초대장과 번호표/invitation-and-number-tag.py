n, g = map(int, input().split())

invite = set()
invite.add(1)
value = 0
t= 0

g_lst = []

for i in range(g) :
    lst = list(map(int, input().split()))
    g_lst.append(lst)

while True :
    some = 0
    for i in range(g) :
        lst = g_lst[i]
        
        num = lst[0]
        member = lst[1:]

        count = 0

        for m in member :
            if m in invite :
                count +=1
            else :
                not_inv = m

        if num - count == 1 :
            some +=1
            invite.add(not_inv)
    
    if some == 0 :
        break



print(len(invite))