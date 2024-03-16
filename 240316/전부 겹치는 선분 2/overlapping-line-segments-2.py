import sys

input = sys.stdin.readline

n = int(input())

infomation = [list(map(int, input().split())) for _ in range(n)]

count = 0
for num in range(n) :
    
    lane = [0]*101
    for p in range(n) :
        if num == p :
            continue
        
        for x in range(infomation[p][0], infomation[p][1]+1) :
            lane[x] += 1
        
    for value in lane :
        if value == n-1 :
            print('Yes')
            count +=1
            break
    if count != 0 :
        break

if count == 0 :
    print('No')