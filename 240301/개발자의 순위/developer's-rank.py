import sys

input = sys.stdin.readline

k,n = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(k)]

result = 0

for i in range(1,n+1) :

    for j in range(1,n+1) :
        if i == j :
            continue
        count = 0
        for ele in arr :
            if  ele.index(j) < ele.index(i) :
                count +=1
        if count == k:
            result +=1


print(result)