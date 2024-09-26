from sortedcontainers import SortedSet


n,m = map(int, input().split())

# s = SortedSet()


grid = list(map(int, input().split()))

# prev_length 랑 add한 length랑 비교 앉았는지 확인하기

maxi = 0
s =  SortedSet()
count = 0
for i in range(n) :
    t= grid[i]
    while True :
        if t == 0   :
            maxi = max(len(s),maxi)
            count +=1
            break
        if t not in s :
            s.add(t)
            break
        
        else :
            t -=1
    
    if count != 0 :
        break

print(len(s))