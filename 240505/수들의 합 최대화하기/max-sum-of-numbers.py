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

        maxi = max(maxi,result)
        result = 0
        return
    
    for p in range(n) :
        if visited_x[p] :
            continue
        for q in range(n) :
            if visited_y[q] :
                continue
            result += matrix[p][q]
            visited_x[p] = True
            visited_y[q] = True

            choose(num+1)
        
            visited_x[p] = False
            visited_y[q] = False


    

choose(1)
print(maxi)