import sys


input = sys.stdin.readline


n = int(input())
answer = []

matrix = [list(map(int, input().split())) for _ in range(n)]


visited_x = [False]*n
visited_y = [False]*n


maxi = 0 
result = 0
def choose(num) :
    global result
    
    global maxi

    if num == n +1 :

        maxi = max(result,maxi)
        result = 0
        return

    for i in range(n) :
        for j in range(n) :
            if visited_x[i] == True or visited_y[j] == True :
                continue

            result += matrix[i][j]

            visited_x[i] = True
            visited_y[j] = True

            choose(num +1)

            visited_x[i] = False
            visited_y[j] = False


choose(1)
print(maxi)