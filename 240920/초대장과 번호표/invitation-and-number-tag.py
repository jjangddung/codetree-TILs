n, g = map(int, input().split())

invite = set()
invite.add(1)


for i in range(g) :
    lst = list(map(int, input().split()))
    num = lst[0]
    member = lst[1:]

    count = 0

    for m in member :
        if m in invite :
            count +=1
        else :
            not_inv = m
    
    if num - count == 1 :
        invite.add(not_inv)

print(len(invite))