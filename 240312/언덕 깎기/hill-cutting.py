import sys

input = sys.stdin.readline


n = int(input())

mount =[int(input()) for _ in range(n)]

# 최솟값이랑 최대값을 정하고 그에 맞춰서 값들을 정해보기

low_mount = min(mount)
high_mount = max(mount)


mini = 1000000000

for min_value in range(low_mount,high_mount+1) :
    for max_value in range(min_value,min_value+18) :
        total = 0 

        for mountain in  mount :
            if mountain < min_value :
                value = min_value- mountain
                value = value*value
            elif min_value <= mountain <= max_value :
                value = 0
            else  :
                value = (mountain- max_value)*(mountain-max_value)
            total += value 

        mini = min(total,mini)

print(mini)