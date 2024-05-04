import sys


input = sys.stdin.readline


n = int(input())
answer = []


visited_list = [False] *(n+1)

def choose(curr_num) :
    
    if curr_num == n +1 :
        print(*answer)
        return

    for i in range(1,n+1) :
        if  visited_list[i] :
            continue
        
        visited_list[i] = True
        answer.append(i)

        choose(curr_num+1)
        answer.pop()
        visited_list[i] = False


choose(1)