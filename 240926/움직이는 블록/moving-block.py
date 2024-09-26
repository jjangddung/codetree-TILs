n = int(input())



grid = [
    int(input())
    for _ in range(n)
]


standard = sum(grid)//n


plus_lst = []
# minus_lst = []
for g in grid :
    if g > standard :
        plus_lst.append(g-standard)
    
    


print(sum(plus_lst))