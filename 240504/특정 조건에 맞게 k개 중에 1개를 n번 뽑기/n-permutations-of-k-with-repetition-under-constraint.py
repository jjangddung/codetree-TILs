k,n = map(int,input().split())

answer = []

def checking(num) :
    if num == n  :
        print(*answer, sep = " ")
        return

    for ele in range(1,k+1) :
        if num >=2 and answer[-1] == ele and answer[-2] == ele :
            continue
        answer.append(ele)
        checking(num +1 )
        answer.pop()

    return


checking(0)