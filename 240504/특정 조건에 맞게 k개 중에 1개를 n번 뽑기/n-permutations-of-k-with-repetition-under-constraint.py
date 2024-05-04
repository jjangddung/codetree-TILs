k,n = map(int,input().split())

answer = []

def print_answer() :
    print(*answer, sep = " ")


def checking(num) :
    if num == n +1 :
        print_answer()
        return

    for ele in range(1,k+1) :
        if num >= 3 and answer[-1] == ele and answer[-2] == ele :
            continue
        answer.append(ele)
        checking(num +1 )
        answer.pop()

    return


checking(1)