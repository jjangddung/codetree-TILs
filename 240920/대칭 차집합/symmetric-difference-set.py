num_a, num_b = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

k = a-b
t = b - a

set_g = set()

for v in k :
    set_g.add(v)

for v in t :
    set_g.add(v)

print(len(set_g))