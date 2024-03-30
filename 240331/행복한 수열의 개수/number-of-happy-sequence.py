import sys

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

new_line_list = []
result = 0
for i in range(n) :
    new_line_1 = []
    new_line_2 =  matrix[i]

    for j in range(n) :
        new_line_1.append(matrix[j][i])
    
    new_line_list.append(new_line_1)
    new_line_list.append(new_line_2)

# print(new_line_list)

for line in new_line_list :
    count = 1
    maxi = 0
    for p in range(n-1) :
        if line[p] == line[p+1] :
            count +=1
            # print("line과 count : ", line, count)

            if p == n-2 :
                maxi = max(count,maxi)
                
        else :
            maxi = max(count,maxi)
            count = 1
    # print(maxi)
    # print(line, maxi)
    if maxi >= m :
        result +=1

print(result)