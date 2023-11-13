import sys

input  = sys.stdin.readline

question = list(map(str, input().split()))

N = int(question[0])

answer_list = []

for i in range(N) :
    answer_list.append(str(input().rstrip()))



answer_list = sorted(answer_list)

k = int(question[1])
length = len(question[2])

result_list = []

for i in answer_list :
    if i[0:length] == question[2] :
        result_list.append(i)





print(result_list[k-1])