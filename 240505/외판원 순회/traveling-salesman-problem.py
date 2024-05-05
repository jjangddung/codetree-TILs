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
            result += matrix[answer[i-1]][answer[i]]
        result += matrix[0][answer[0]]
        result += matrix[answer[-1]][0]

        if result < mini :
            print(*answer)


        mini = min(result,mini)


        # for p in range(n-1) :
            # index = answer[p]
            # if p == 0 :
                # result += matrix[0][index]
            # elif p == n-2 :
                # result += matrix[index][0]
            # else :
                # index_2 = answer[p-1]
                # result += matrix[index_2][index]
            # 
            # mini = min(result,mini)

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