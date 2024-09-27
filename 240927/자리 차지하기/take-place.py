from sortedcontainers import SortedSet


n,m = map(int, input().split())

arr = list(map(int, input().split()))


# 빈자리에 대해 sortedset

seats = SortedSet(range(1,m+1))

ans = 0


for elem in arr :
    idx = seats.bisect_right(elem) # elem 보다  더 큰 수의 index 출력


    if idx != 0 :
        idx -=1 
        seats.remove(seats[idx])

        ans+=1
    else :
        break

print(ans)