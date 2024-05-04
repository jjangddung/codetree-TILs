n, m = map(int, input().split())

answer = []
# choose 에서 범위를 정해주기

def choose(num,p) :
    if num == m + 1 :
        print(*answer, sep = " ")
        return


    for i in range(p, n +1 ) :
        answer.append(i)
        choose(num +1,i+1)
        answer.pop()

choose(1,1)