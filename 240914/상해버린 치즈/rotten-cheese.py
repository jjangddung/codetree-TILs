import sys

input = sys.stdin.readline


N,M,D,S = map(int, input().split())


cheese_lst = [] # 누가,몇번째, 언제

result = []

for _ in range(D) :
    p,m,t = map(int, input().split())

    cheese_lst.append([p,m,t])

cons_lst = []
sick_lst = []
for _ in range(S) :
    p,t = map(int, input().split())
    sick_lst.append(p)
    

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
    count_lst  = 0
    new_lst = []
    for case in cheese_lst :
        if ans == case[1]  :
            new_lst.append(case[0])
    
    # print(new_lst)
    new_lst = set(new_lst)
    new_lst = list(new_lst)
    if len(new_lst) >= S :
        
        for t in range(len(new_lst)) :
            human.append(new_lst[t])
            


human = set(human)

print(len(human))