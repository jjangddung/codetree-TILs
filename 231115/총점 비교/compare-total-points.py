import sys

input = sys.stdin.readline


N = int(input())



class Total() :
    def __init__(self,Tuple) :
        self.name = Tuple[0]
        self.kor  = int(Tuple[1])
        self.eng  = int(Tuple[2])
        self.math = int(Tuple[3])
        self.grading()
    
    def grading(self) :
        self.grade = int(self.kor + self.eng + self.math)



student_list  = []




for _ in range(N) :
    person = tuple(map(str, input().split()))
    student_list.append(Total(person))

student_list.sort(key = lambda x: x.grade)

for person in student_list:
    print(person.name, person.kor, person.eng, person.math)