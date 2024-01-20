import sys


input = sys.stdin.readline

n = int(input())
class Priv() :
    def __init__(self,Tuple) :
        self.seq   =   Tuple[2]
        self.height =   int(Tuple[0])
        self.weight = int(Tuple[1])



people_list = []
for i in range(n) :
    h,w = map(int, input().split())
    person = (h,w,i+1)
    people_list.append(Priv(person))


new_list =sorted(people_list, key=lambda x: (x.height, -x.weight))
# old_list =sorted(people_list, key=lambda x: -x.height)
for person in new_list :
    print(person.height, person.weight,person.seq)

print()