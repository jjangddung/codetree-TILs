import sys

input = sys.stdin.readline


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
# print(matrix)
answer = []
mini = 5000000

visited = [False] * (n+1)
def choose(num) :
    global mini


    if num == n  :
        result = 0


        for i in range(1,len(answer)) :
            a = matrix[answer[i-1]][answer[i]]
            if a == 0 :
                return
            result += a

        b = matrix[0][answer[0]]
        c = matrix[answer[-1]][0]

        if b == 0 or c == 0 :
            return
        result = result + b + c 

        mini = min(result,mini)

        return

    
    for p in range(1,n) :
        if visited[p] :
            continue

        answer.append(p)
        visited[p] = True

        choose(num +1)

        visited[p] = False
        answer.pop()

choose(1)
print(mini)