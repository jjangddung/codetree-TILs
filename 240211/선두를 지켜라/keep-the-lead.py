import sys


input = sys.stdin.readline



n,m = map(int, input().split())


n_list = [list(map(int, input().split()))for _ in range(n)]

m_list = [list(map(int, input().split()))for _ in range(m)]

start_1  = [0]
start_2  = [0]


for arr in n_list :
    v = arr[0]
    t = arr[1]
    if len(start_1) == 1 :
        start = start_1[0]
    
    else :
        start = start_1[-1]
    
    for time in range(t) :
        start = start + v
        start_1.append(start)

for arr in m_list :
    v = arr[0]
    t = arr[1]
    if len(start_2) == 1 :
        start = start_2[0]
    
    else :
        start = start_2[-1]
    
    for time in range(t) :
        start = start + v
        start_2.append(start)


length = len(start_2)
count = 0
result_list = []

for i in range(1,length) :
    result =  start_1[i]-start_2[i]
    if result < 0 :
        result = -1
        result_list.append(result)
    
    if result > 0 :
        result = 1
        result_list.append(result)

    


r_length = len(result_list)

for i in range(r_length-1) :
    if result_list[i] != result_list[i+1] :
        count+=1

print(count)