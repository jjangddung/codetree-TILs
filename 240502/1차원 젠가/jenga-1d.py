def f(A, s, e) :
    temp = []

    for  i in range(len(A)) :
        if s <= i <= e :
            continue
        temp.append(A[i])
    return temp 


N = int(input())


A = [int(input()) for _ in range(N)]


for _ in range(2) :
    s, e = map(int, input().split())
    A = f(A, s-1, e-1)

print(len(A))
print(*A, sep = "\n")