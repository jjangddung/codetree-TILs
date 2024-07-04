import sys

input = sys.stdin.readline


n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def in_range(x,y) :
    return 0 <= x < n and 0 <= y < m 

maxi = -1 

def checking(x,y,width,height) :
    for t in range(height) :
        for p in range(width):
            if not in_range(x+t,y+p) :
                return False
            if matrix[x+t][y+p] <= 0 :
                return False

    return True

def final_checking(h,w,n,m) :
    for p in range(n) :
        for q in range(m) :
            if checking(p,q,w,h) == True :
                return True 

    return False

for h in range(1,n+1) :
    for w in range(1,m+1) :
        if final_checking(h,w,n,m)  == True :
            maxi = max(maxi, h*w)
                
print(maxi)