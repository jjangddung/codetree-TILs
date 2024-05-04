import sys

input = sys.stdin.readline

k,n = map(int,input().split())

answer = []

def print_answer() :
    print(*answer, sep = "")


def checking(num) :
    if num == n+1 :
        print_answer()
        return

    for ele in range(1,k+1) :
        answer.append(ele)
        checking(num+1)
        answer.pop()

    return


checking(1)