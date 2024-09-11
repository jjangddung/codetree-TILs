import sys

n,k = map(int, input().split())

grid = list(map(int, input().split()))

grid.sort()

origin = {}
new_origin = {}
# maximum_lst = []


for i in range(n) :
    v= grid[i]

    if v not in origin :
        origin[v] = 1
    else :
        origin[v] +=1  # origin[v] == 개수
    
origin = sorted(origin.items(),key = lambda x :(x[1],x[0]),reverse = True) # value 값을 기준으로 정렬
# origin.items(): 이 메서드는 사전의 모든 키-값 쌍을 튜플 형태로 반환

for i in range(k) :
    print(origin[i][0], end = " ")