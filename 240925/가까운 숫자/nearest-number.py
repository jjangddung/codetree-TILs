from sortedcontainers import SortedSet
import sys

s = SortedSet()



s.add(0)

n = int(input())
grid = list(map(int, input().split()))

for g in grid :
    s.add(g)
    mini = sys.maxsize

    for num in s :
        index = s.bisect_right(num)

        if index != len(s) :
            result = abs(s[index]- num)
        
        mini = min(result, mini)
    
    print(mini)