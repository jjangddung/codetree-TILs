import sys

input = sys.stdin.readline


class Info() :
    def __init__(self, Tuple) :
        self.name    = Tuple[0]
        self.height  = int(Tuple[1])
        self.weight  = int(Tuple[2])

N = int(input())


student_list = []
for _ in range(N) :
    person = tuple(map(str, input().split()))
    student_list.append(Info(person))

student_list.sort(key = lambda x : (x.height, -x.weight))


for person in student_list :
    print(person.name, person.height, person.weight)