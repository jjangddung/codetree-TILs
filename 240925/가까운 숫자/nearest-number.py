from sortedcontainers import SortedSet
import sys

s = SortedSet()



s.add(0)

n = int(input())
grid = list(map(int, input().split()))
mini = sys.maxsize

i = 0

for g in grid :
    

    if i == 0 :
        s.add(g)
        mini = s[1] - s[0]
    
    else :
        index1 = s.bisect_right(g)
        # index2 = index1 - 1

        if 0 < index1 < len(s) : 
            result = min(abs(s[index1]- g), abs(s[index1-1] - g))
        
        elif index1 == len(s) :
            result = abs(s[index1-1]-g)
        
        elif index1 == 0 :
            result = abs(s[index1]-g)

        mini = min(result,mini)
        s.add(g)
    print(mini)
    i +=1