n1,n2 = map(int , input().split())


lst1 = list(map(int, input().split()))

lst2 =  list(map(int, input().split()))
count = 0
for i in range(n1) :
    if i+n2 > n1 :
        print('No')
        count +=1
        break
    new_lst = lst1[i:i+n2]

    if new_lst == lst2 :
        print("Yes")
        count +=1
        break



if count == 0 :
    print('No')