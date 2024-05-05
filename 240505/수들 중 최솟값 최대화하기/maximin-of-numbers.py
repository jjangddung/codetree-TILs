import sys

input = sys.stdin.readline

n = int(input())

answer = []


matrix = [list(map(int, input().split())) for _ in range(n)]


mini  = 0

visited_list = [False] *n


def choose(curr_num) :
    global mini

    if curr_num  == n +1 :
        result_list = []


        for p in range(n) :
            result_list.append(matrix[p][answer[p]])

        result = min(result_list)

        mini = max(mini,result)

        return
    
    for i in range(n) :
        if visited_list[i] :
            continue
        
        answer.append(i)
        visited_list[i] = True

        choose(curr_num +1 )

        answer.pop()
        visited_list[i] = False


choose(1)
print(mini)