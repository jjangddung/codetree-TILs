k,n = map(int,input().split())

answer = []

def print_answer() :
    print(*answer, sep = " ")


def checking(num) :
    if num == n+1 :
        print_answer()
        return

    for ele in range(1,k+1) :
        t = len(answer)
        if  t < 2 :
            answer.append(ele)
            checking(num+1)
            answer.pop()
        else :
            if answer[t-1] == ele :
                if answer[t-1] != answer[t-2] :
                    answer.append(ele)
                    checking(num+1)
                    answer.pop()
            else :
                answer.append(ele)
                checking(num+1)
                answer.pop()


    return


checking(1)