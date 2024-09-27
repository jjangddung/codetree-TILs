n, m = map(int, input().split())
grid = list(map(int, input().split()))

parent = {}

def find(x):
    if x not in parent:
        return x
    parent[x] = find(parent[x])
    return parent[x]

count = 0
for t in grid:
    p = find(t)
    if p == 0:
        continue
    parent[p] = p - 1
    count += 1

print(count)