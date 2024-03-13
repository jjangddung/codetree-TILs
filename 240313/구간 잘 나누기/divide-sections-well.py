import sys

input = sys.stdin.readline

n,m = map(int, input().split())


arr = list(map(int, input().split()))

# list 중간에 0을 추가하는 방법?
#0을 만나거나 끝 부분이면 종료
# list 길이는 n+m-1
# combination 구현 >> n+m-1Cn

real = [0]*(n+m-1)

# print(real)
answer = []
answer_list = []


global mini
mini = 10000000


def checking(p) :
    if len(answer) == 0 :
        return True

    else :
        if p - max(answer) <=1 :
           return False
        else :
            return True

def store(num) :
    global mini
    if num == m-1 :
        # answer_list.append(answer)
        # print(answer)
        num_list = []
        for p in range(n+m-1) :
            if not p in answer :
                num_list.append(p)
        real = [0]*(n+m-1)
        for t in range(n) :
            real[num_list[t]] = arr[t]
        
        maxi = 0
        total = 0

        for number in range(n+m-1) :
            if real[number] == 0 or number == n+m-2 :
                total += real[number]
                maxi = max(total,maxi)
                if maxi > mini :
                    break
                total = 0
            
            else :
                total += real[number]
        
        mini = min(mini,maxi)

        

        return

    for i in range(1,n+m-2) :
        if checking(i) == True :
            answer.append(i)
            store(num+1)
            answer.pop()
    
    return


store(0)
# print(answer_list)

print(mini)