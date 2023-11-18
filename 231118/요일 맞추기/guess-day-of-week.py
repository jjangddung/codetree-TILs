import sys


input = sys.stdin.readline


m_1,d_1,m_2,d_2 = map(int, input().split())


day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

reverse_day = ['Mon','Sun','Sat','Fri','Thu','Wed','Tue']

date_1 = 0
date_2 = 0

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(m_1) :
    date_1 += month[i]

date_1 += d_1

for i in range(m_2) :
    date_2 += month[i]

date_2 += d_2

result = date_2 - date_1

if result >= 0 :
    result = result%7
    print(day[result])

else :
    result = -result
    result = result%7
    print(reverse_day[result])