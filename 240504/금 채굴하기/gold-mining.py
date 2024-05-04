import sys

input = sys.stdin.readline


n , m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n) :
    for j in range(n) :
        origin_x, origin_y = i,j

        k = 1 
        
        while 2*k -1 < n :
            total_sum = 0
            count = 0
            cost = - 2*(k**2) -2*k -1
            for x in range(n) :
                for y in range(n) :
                    distance = abs(x-origin_x) + abs(y-origin_y)
                    if distance <=   k and matrix[x][y] == 1 :
                        total_sum += matrix[x][y] * m
                        count += 1

            
            total_cost = total_sum + cost
            k +=1
            if total_cost >= 0 :
                result = max(count, result)

print(result)