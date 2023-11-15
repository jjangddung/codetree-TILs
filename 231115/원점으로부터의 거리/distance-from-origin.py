import sys

input = sys.stdin.readline

class Distance() :
    def __init__(self,Tuple, seq) :
        self.x_dis = int(Tuple[0])
        self.y_dis = int(Tuple[1])
        self.calculate()
        self.seq = seq
    
    def calculate(self) :
        self.man = abs(self.x_dis) + abs(self.y_dis)


N = int(input())

distance_list = []

for i in range(N) :
    person = tuple(map(int, input().split()))
    distance_list.append(Distance(person,i+1))


distance_list.sort(key = lambda x : (x.man))

for dis in distance_list :
    print(dis.seq)