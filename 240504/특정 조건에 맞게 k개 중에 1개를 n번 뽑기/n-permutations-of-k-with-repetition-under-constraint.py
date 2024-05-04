k,n = map(int,input().split())

answer = []

def print_answer() :
    print(*answer, sep = " ")


def checking(num) :
    if num == n+1 :
        print_answer()
        return

    for ele in range(1,k+1) :
        if num < 3 :
            answer.append(ele)
            checking(num+1)
            answer.pop()
        else :
            if answer[num-1] != answer[num] and answer[num-1] != answer[num-2]:
                answer.append(ele)
                checking(num+1)
                answer.pop()

    return


checking(1)