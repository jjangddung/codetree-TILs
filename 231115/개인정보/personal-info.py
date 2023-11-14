import sys


input = sys.stdin.readline


class Priv() :
    def __init__(self,Tuple) :
        self.name   =   Tuple[0]
        self.height =   int(Tuple[1])
        self.weight = float(Tuple[2])



people_list = []
for i in range(5) :
    person = tuple(map(str, input().split()))
    people_list.append(Priv(person))


new_list =sorted(people_list, key=lambda x: x.name)
old_list =sorted(people_list, key=lambda x: -x.height)
print('name')
for person in new_list :
    print(person.name, person.height, person.weight)

print()




print('height')
for person in old_list :
    print(person.name, person.height, person.weight)