n,m = map(int, input().split())



jew_lst = [
    list(map(int, input().split()))
    for _ in range(n)
]

value_lst = []


for jew in jew_lst :
    jew_w,jew_v = jew
    jew_t = jew_v/jew_w
    value_lst.append([jew_w,jew_v,jew_t])

# print(value_lst)

value_lst = sorted(value_lst, key=lambda x: x[2], reverse = True)

# print(value_lst)

result_v = 0
result_w = 0

for jewery in value_lst :
    if result_w + jewery[0] <= m :
        result_v += jewery[1]
        result_w += jewery[0]
    
    else :
        result_v += (m-result_w) * jewery[2]
        break
    



print(f'{result_v:.3f}')