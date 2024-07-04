import sys

input = sys.stdin.readline


n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def in_range(x,y) :
    return 0 <= x < n and 0 <= y < m 

maxi = -1 

def checking(x,y,width,height) :
    for t in range(height+1) :
        for p in range(width+1):
            if not in_range(x+t,y+p) :
                return False
            if matrix[x+t][y+p] < 0 :
                return False

    return True



for h in range(n) :
    for w in range(m) :
        for p in range(n) :
            for q in range(m) :
                if matrix[p][q] < 0 :
                    total = -1

                if checking(p,q,w,h) == True :
                    total = (w+1)*(h+1)
                #     print(p,q,w,h)
                maxi = max(maxi,total)
                




print(maxi)