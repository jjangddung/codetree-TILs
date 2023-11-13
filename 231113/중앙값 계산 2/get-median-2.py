import sys

input = sys.stdin.readline


n = int(input())

que_list = list(map(int, input().split()))
answer_list = []



for i in range(n) :
    answer_list.append(que_list[i])
    answer_list.sort()
    if i == 0 :
        print(answer_list[0], end = " ")
    elif i % 2 == 0 :
        num = i//2 
        print(answer_list[num], end= " ")