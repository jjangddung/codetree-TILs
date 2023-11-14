import sys

input = sys.stdin.readline


class Rain :
    def __init__(self,data_list) :
        self.year = data_list[0]
        self.date = data_list[1]
        self.weather = data_list[2]


N = int(input())
rain_data = []
for _ in range(N) :
    data = list(map(str, input().split()))
    problem = Rain(data)
    if problem.weather == 'Rain' :
        rain_data.append(data)

rain_data.sort()

for j in rain_data[0] :
    print(j, end= " ")