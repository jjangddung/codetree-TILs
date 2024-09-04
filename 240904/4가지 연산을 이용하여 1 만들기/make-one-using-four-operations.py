# 가능한 방법을 전부 다 모색하면서 돌기  //

from collections import deque
import sys




n = int(input())




q = deque()

visited = [False]*3000001



step = [0]*3000001


def push(num,s) :
    step[num] = s
    visited[num] = True
    q.append(num)


def calculate(num,s) :
    if s == 0 :
        num +=1
    elif s == 1 :
        num -=1 

    elif s == 2 :
        if num %2  == 0 :
            num//=2

        else :
            num = 3000000

    else :
        if num % 3 == 0 :
            num = num//3
        
        else :
            num = 3000000

    return num
        
    
def bfs() :
    sign = [0,1,2,3] #+ - //3 //2
    while q :
        number = q.popleft()
        for cal in sign :
            new_num = calculate(number,cal)

            if 0 <= new_num < 3000000 and not visited[new_num] :
                push(new_num,step[number]+1)

push(11,0)
bfs()
print(step[1])