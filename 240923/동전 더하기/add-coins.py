n,k = map(int, input().split())


coin_lst = [
    int(input())
    for _ in range(n)
]

coin_lst = coin_lst[::-1]


value = 0
coin = 0
i = 0
while value != k :
    
    if value + coin_lst[i] <= k :
        coin +=1
        value += coin_lst[i]
    
    else :
        i+=1

print(coin)