from sortedcontainers import SortedSet
import sys

s = SortedSet()



s.add(0)

n = int(input())
grid = list(map(int, input().split()))
mini = sys.maxsize

i = 0

for g in grid :
    s.add(g)

    if i == 0 :
        mini = s[1] - s[0]
    
    else :
        index1 = s.bisect_right(g)
        index2 = index1 - 2

        if index1 < len(s) and  0< index2 : 
            result = min(abs(s[index1]- g), abs(s[index2] - g))
        
        elif 0 < index2 :
            result = abs(s[index2]-g)
        
        elif index1 < len(s) :
            result = abs(s[index1]-g)

        mini = min(result,mini)
    
    print(mini)
    i +=1