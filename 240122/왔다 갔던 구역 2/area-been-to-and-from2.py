import sys


input = sys.stdin.readline


n = int(input())


start = 0
end = 0

arr = [0 for _ in range(3001)]



for i in range(n) :
    x , d = map(str, input().split())
    x = int(x)
    start = end 
    if d == 'R' :
        end += x
        for j in range(start+1000, end+1000) :
            arr[j]  += 1
        
    else :
        end -= x
        for j in range(end+1000, start+1000) :
            arr[j]  += 1


sum = 0

for k in arr :
    if k >= 2:
        sum +=1


print(sum)