import sys

# x1,y1,x2,y2
n,m = map(int, input().split())

grid = [list(map(int , input().split())) for _ in range(n)]

def overlap(arr1,arr2) :
    x1,y1,x2,y2 = arr1
    x3,y3,x4,y4 = arr2

    count = 0

    for i in range(x1,x2+1):
        for j in range(y1,y2+1) :
            if x3 <= i <= x4 and y3 <= j <= y4 :
                return True
    
    return False


def square_value(arr) :
    x1,y1,x2,y2  = arr
    total = 0
    # count = 0
    for i in range(x1,x2+1) :
        for j in range(y1,y2+1) :
            total += grid[i][j]
        
    
    return total

maxi = -sys.maxsize

for i in range(n) :
    for j in range(m) :
        for k in range(i,n) :
            for l in range(j,m) :
                arr1 = [i,j,k,l]
                for p in range(n) :
                    for q in range(m):
                        for r in range(p,n) :
                            for t in range(q,m) :
                                value = 0
                                arr2 = [p,q,r,t]
                                
                                if not overlap(arr1,arr2) :
                                    # print(arr1,arr2)
                                    value += square_value(arr1)
                                    value += square_value(arr2)
                                    maxi = max(value,maxi)
                                    # print(maxi)

print(maxi)