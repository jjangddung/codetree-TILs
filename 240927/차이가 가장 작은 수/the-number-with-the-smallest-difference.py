import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline


n,m = map(int, input().split())

s = SortedSet()

for _ in range(n) :
    s.add(int(input()))



mini = sys.maxsize

for v in s :
    std = v + m

    idx=  s.bisect_left(std) # v와 최소 m 이상만큼 차이나는 수 발견 ,,,,
                             # 만약 idx = 0 or len(s)면 없는거임
        
    
    if idx == 0  or idx == len(s) :
        continue
    
    result = s[idx] -v 

    mini = min(result, mini)

print(mini)