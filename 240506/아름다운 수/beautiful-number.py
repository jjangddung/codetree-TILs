import sys

input = sys.stdin.readline

n = int(input())

answer = []
count  = 0

                
answer_seet  = [[1],[2,2],[3,3,3],[4,4,4,4]]


def num_apend(ele) :
    for _ in range(ele) :
        answer.append(ele)
    
    return 


def num_pop(ele) :
    for _ in range(ele) :
        answer.pop()
    return
    


def checking(num) :
    global count
    if num <= n +1 and len(answer) >=n :
        if len(answer) == n:
            # print(*answer)
            count +=1
        return


    for ele in range(1,5) :
        num_apend(ele)
        checking(num + 1)
        num_pop(ele)

    return


checking(1)
print(count)