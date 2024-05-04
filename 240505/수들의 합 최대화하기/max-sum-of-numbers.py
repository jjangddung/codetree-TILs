import sys


input = sys.stdin.readline


n = int(input())
answer = []

matrix = [list(map(int, input().split())) for _ in range(n)]


visited_list = [False]*n

maxi = 0 

def choose(num) :
    global maxi

    if num == n +1 :
        result = 0

        for t in range(n) :
            result += matrix[t][answer[t]]
        maxi = max(result, maxi) 
        return

    for i in range(n) :
        if visited_list[i]:
            continue

        answer.append(i)
        visited_list[i] = True
        
        choose(num +1)
        answer.pop()
        visited_list[i] = False


choose(1)
print(maxi)