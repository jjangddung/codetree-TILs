n,m = map(int, input().split())


a_lst = []

start_time = 1

a_pos = {}
b_pos = {}
a_pos[0]= 0
b_pos[0] = 0

for _ in range(n) :
    v,t = map(int, input().split())

    for i in range(start_time,start_time+t) :
        a_pos[i] = v+ a_pos[i-1]
    
    start_time = start_time+t


maxi = start_time-1

start_time = 1

for _ in range(m) :
    v,t = map(int, input().split())

    for i in range(start_time,start_time+t) :
        b_pos[i] = v+ b_pos[i-1]
    
    start_time = start_time+t

# print(maxi)
# print(a_pos)
# print(b_pos)




prev= a_pos[1] - b_pos[1]


def win(result) :
    if result < 0 :
        return  0
    elif result > 0 :
        return 1
    else :
        return 2


prev = win(prev)
count = 1 
for i in range(2,maxi+1) :
    present = a_pos[i] -b_pos[i]
    present = win(present)

    if prev != present :
        # print(i)
        count +=1
    
    prev = present

print(count)