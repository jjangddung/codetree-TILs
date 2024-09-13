# 2월은 29일까지 있음..
# 날짜 차이로 접근 ??? 그 날까지의 시간 차로 빼기

lst = [0,31,29,31,30,31,30,31,31,30,31,30,31]

value = [1,0,0,0,0,0,0]


m1,d1,m2,d2 = map(int, input().split())




A = str(input())
day1 = 0

for i in range(1,m1+1) :
    if i != m1 :
        day1 += lst[i]
    
    else :
     
        day1 += d1

day2 = 0

for i in range(1,m2+1) :
    if i != m2 :
        day2 += lst[i]
    
    else :
        day2 += d2

result = day2-day1

# print(result)

for date in range(result+1) :
    new_date = date%7
    value[new_date] +=1

# print(value)
if A == 'Mon' :
    print(value[0])

elif A == "Tue" :
    print(value[1])

elif A == "Wed" :
    print(value[2])

elif A == "Thu" :
    print(value[3])

elif A == "Fri" :
    print(value[4])

elif A == "Sat" :
    print(value[5])

elif A == "Sun" :
    print(value[6])