import sys

input = sys.stdin.readline


class People() :
    def __init__(self, name, height, weight) :
        self.name = name
        self.height = height
        self.weight = weight




N = int(input())

people_list = []

for _ in range(N) :
    person = tuple(map(str, input().split()))
    people_list.append(person)


people_list.sort(key = lambda x: x[1])

for person in people_list :
    for j in person:
        print(j, end= " " )
    print()