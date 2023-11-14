import sys

input = sys.stdin.readline


class Student :
    def __init__(self,Tuple,num) :
        self.height = int(Tuple[0])
        self.weight = int(Tuple[1])
        self.num = num+1






N = int(input())
student_list = []

for i in range(N) :
    person = tuple(map(int, input().split()))
    student_list.append(Student(person,i))

student_list.sort(key = lambda x: (-x.height, -x.weight))

for student in student_list :
    print(f'{student.height} {student.weight} {student.num}')