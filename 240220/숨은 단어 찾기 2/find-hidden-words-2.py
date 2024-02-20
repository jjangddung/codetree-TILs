import sys

input = sys.stdin.readline


n,m = map(int, input().split())

arr = []

for i in range(n) :
    string  = input()
    small = []
    for i in range(m) :
        small.append(string[i])
    arr.append(small)

# print(arr)
# q = "abc"
# p = "def"



# print(arr)
dxs = [1,1,1,0] # 오른쪽 대각선, 왼쪽 대각선, 상하, 좌우
dys = [1,-1,0,1]

def in_range(x,y)  :
    return 0 <= x < n and 0 <= y < m 

final = 0

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == "E" :
            # print(i,j)
            for direct in range(4) :
                result = 0
                result = str(0)
                
                for count in range(-1,2) :
                    nx , ny = i + count*dxs[direct] , j + count*dys[direct]
                    if not in_range(nx,ny) :
                        # print(f'i = {i}, j = {j} 에서 {direct}인 방향에서 범위를 벗어났습니다.')
                        break
                    else :
                        result += str(arr[nx][ny])
                        # print(result)

                if result == "0LEE" or result == "0EEL" :
                    final +=1
                    # print(result,i,j)


print(final)