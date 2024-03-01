import sys

input = sys.stdin.readline

n = int(input())

ele = [list(map(int, input().split())) for _ in range(n)]




result = 0

for i in range(n-2) :
    
    for j in range(i+1,n-1) :
        for k in range(j+1,n) :
            matrix = [0]* 102

            new_list = [i,j,k]
            mid = 0
            for p in range(n) :
                if p in new_list :
                    continue
                start, end  = ele[p][0], ele[p][1]
                for cont in range(start,end+1) :
                    matrix[cont] +=1

            count = 0

            for mid in matrix :
                if mid >= 2:
                    count +=1
            if count == 0 :
                result+=1
                # print(i,j,k)           
print(result)