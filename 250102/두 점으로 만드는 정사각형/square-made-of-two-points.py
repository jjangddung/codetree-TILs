squre1 = list(map(int, input().split()))
squre2 = list(map(int, input().split()))

w1 = max(squre1[0],squre1[2],squre2[0],squre2[2])
w2 = min(squre1[0],squre1[2],squre2[0],squre2[2])
h1 = max(squre1[1],squre1[3],squre2[1],squre2[3])
h2 = min(squre1[1],squre1[3],squre2[1],squre2[3])

length = max((w1-w2),(h1-h2))

print(length**2)