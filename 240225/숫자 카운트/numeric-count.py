import sys

input = sys.stdin.readline

n = int(input())

matrix =[list(map(int, input().split())) for _ in range(n)]

# print(matrix[0])
result_arr = []


for i in range(1,10) :

    for j in range(1,10) :

        for k in range(1,10) :
            
            result = 0
            new_list = [i,j,k]
            for w in range(n)  :
                # print(new_list, w)
                ele = matrix[w]
                num,s,b = ele[0], ele[1], ele[2]
                num = str(num)
                num_list = [num[0],num[1],num[2]]
                print(num_list)

                first_count = 0
                second_count = 0

                for p in range(3) :
                    if int(num_list[p]) == new_list[p] :
                        first_count +=1
                if first_count != s :
                    break
                
                for q in range(3) :
                    que = new_list[q]
                    if que in num_list and que != num_list[q] :
                        second_count +=1
                
                if second_count != b :
                    break
                result +=1
            if result == n :
                result_arr.append(new_list)

print(result_arr)