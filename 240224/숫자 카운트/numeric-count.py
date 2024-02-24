import sys

input = sys.stdin.readline

n = int(input())

matrix =[list(map(int, input().split())) for _ in range(n)]

result_arr = []


for i in range(1,10) :
    for j in range(1,10) :
        for k in range(1,10) :
            new_list = [i,j,k]
            for ele in matrix :
                num,s,b = matrix[0], matrix[1], matrix[2]
                num = str(num)

                first_count = 0

                for p in range(3) :
                    if num[p] == new_list :
                        first_count +=1
                if first_count != s :
                    break
                
                for q in range(3) :
                    if