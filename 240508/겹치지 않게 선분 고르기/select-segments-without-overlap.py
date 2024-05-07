import sys

input = sys.stdin.readline

n = int(input())


matrix = [list(map(int, input().split())) for _ in range(n)]

visited_list = [0]*(n+1)


answer = []
maxi = 0

def choose(num,start,p) :
    global maxi

    if num == p +1 :
        new_line= [0]*1001
        count = 0

        for ans in answer :
            begin, end = matrix[ans][0],matrix[ans][1]
            for index in range(begin,end+1) :
                if new_line[index] == 0 :
                    new_line[index] = 1
                else :
                    count +=1 
                    break
            if count != 0 :
                break
        if count == 0 :
            maxi = max(p,maxi)                    

        return


    for i in range(start,n) :
        if visited_list[i] :
            continue
        
        answer.append(i)
        visited_list[i] = True

        choose(num+1,i+1,p)
        answer.pop()
        visited_list[i] = False


for x in range(n) :
    choose(0,0,x)

print(maxi+1)