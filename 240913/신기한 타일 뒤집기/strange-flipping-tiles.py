import sys

input = sys.stdin.readline



# 해쉬 맵으로 구현 ?

n = int(input())


black, white, gray = 0,0,0
d = {}



start = 0

for _ in range(n) :
    move, direct = map(str, input().split())
    move = int(move)
    if direct  == 'L' :
        end = start - move +1
        for i in range(start,end-1,-1) :
            d[i] = 0
         
                

    else :
        end = start + move -1

        for i in range(start,end+1) :
            d[i] = 1
                


    start = end


# 0은 흰색 ,1은 검정, 2는 회색


for v in d :
    if d[v] == 0 :
        white +=1
    
    elif d[v] == 1 :
        black +=1
    
    else :
        gray +=1

print(white,black)