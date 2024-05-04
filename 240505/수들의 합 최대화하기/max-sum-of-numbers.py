import sys


input = sys.stdin.readline


n = int(input())
answer = []

matrix = [list(map(int, input().split())) for _ in range(n)]


visited_x = [False]*n
visited_y = [False]*n


maxi = 0 

def choose(num) :
    global result
    
    global maxi

    if num == n +1 :
        result = 0

        for value in answer:
            result += matrix[value[0]][value[1]]
        
        maxi = max(result,maxi)

        return
    
    for p in range(n) :
        if visited_x[p] :
            continue
        for q in range(n) :
            if visited_y[q] :
                continue
            answer.append([p,q])
            visited_x[p] = True
            visited_y[q] = True

            choose(num+1)
            answer.pop()
        
            visited_x[p] = False
            visited_y[q] = False


    

choose(1)
print(maxi)