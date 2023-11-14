import sys

input = sys.stdin.readline


class Subject() :
    def __init__(self,Tuple) :
        self.name = Tuple[0]
        self.kor = int(Tuple[1])
        self.eng = int(Tuple[2])
        self.math = int(Tuple[3])


N = int(input())



people_list = []

for _ in range(N) :
    person = tuple(map(str, input().split()))
    Subject(person)
    people_list.append(Subject(person))

people_list.sort(key = lambda x: (-x.kor, -x.eng, -x.math))

for person in people_list :
    print(person.name, person.kor, person.eng, person.math)