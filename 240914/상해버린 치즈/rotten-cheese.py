import sys

input = sys.stdin.readline


N,M,D,S = map(int, input().split())


cheese_lst = [] # 누가,몇번째, 언제

result = []

for _ in range(D) :
    p,m,t = map(int, input().split())

    cheese_lst.append([p,m,t])

cons_lst = []
for _ in range(S) :
    p,t = map(int, input().split())
    

    for case in cheese_lst :
        if p == case[0]  and t > case[2] :
            cons_lst.append(case[1])
    


count = 0
# print(cons_lst)
cons_lst = set(cons_lst)
cons_lst = list(cons_lst)
# print(cons_lst)
human = []

for ans in cons_lst :
    for case in cheese_lst :
        if ans == case[1] :
            human.append(case[0])

human = set(human)

print(len(human))