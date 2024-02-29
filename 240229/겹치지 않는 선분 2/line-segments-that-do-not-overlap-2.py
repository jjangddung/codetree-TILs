import sys

input = sys.stdin.readline


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

# print(arr-)




count = 0

def check_cross(num) :
    # 선 범위안에 처음부터 아예 안들어가거나, 스타트 지점이 들어간 경우 엔드 지점은 밖에 들어가야함 선 범위에
    ori_start =arr[num][0]
    ori_end = arr[num][1]
    ori = ori_end - ori_start


    for p in range(n) :
        if p == num :
            continue

        start,end = arr[p][0] , arr[p][1]

        new = end - start

        up = ori_start*new - start*ori
        down = new - ori
        if down == 0 :
            continue
            
        result = up/down

        if ori_start<= result <= ori_end :
            return False
            break
    return True






for i in range(n) :
    if check_cross(i) :
        # print(i)
        count +=1

print(count)