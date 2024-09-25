from sortedcontainers import SortedSet


n, m = map(int, input().split())



n_lst = list(map(int, input().split()))

s = SortedSet()


for num in n_lst :
    s.add(num)


for _ in range(m) :
    num= int(input())


    try :

        index = s.bisect_left(num)
        print(s[index])

    
    except :
        print(-1)