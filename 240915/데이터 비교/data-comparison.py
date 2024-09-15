n1 = int(input())

one_lst = list(map(int,input().split()))

one_lst = set(one_lst)

n2  = int(input())

two_lst =  list(map(int, input().split()))

two_set = set(two_lst)

for value in two_lst :
    if value  in one_lst :
        print(1, end= " ")
    
    else :
        print(0, end= " ")