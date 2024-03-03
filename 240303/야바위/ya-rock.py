import sys

input = sys.stdin.readline

n = int(input())




arr = [list(map(int, input().split())) for _ in range(n)]


maxi_grade = 0

for num in range(1,n+1) :
    yabawi = [0]*4
    yabawi[num] = 1
    grade = 0 # 점수

    for count in range(n) :
        a, b, c = arr[count][0], arr[count][1], arr[count][2]
        swap_1 = int(yabawi[a])
        swap_2 = int(yabawi[b])
        yabawi[a] = swap_2
        yabawi[b] = swap_1
        if yabawi[c] == 1 :
            grade +=1
    maxi_grade = max(grade,maxi_grade)


print(maxi_grade)