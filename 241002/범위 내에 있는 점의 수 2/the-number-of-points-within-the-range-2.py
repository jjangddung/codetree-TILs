import sys


n,q = map(int, input().split())


num_lst = list(map(int, input().split()))

# 범위 출력 ....




arr = [0]*1000001 #  1이면 점이 위에 있는거임


for num in num_lst :
    arr[num]  =1


prefix_sum = [0]*(1000001)

prefix_sum[0] = 0

def get_sum(s,e) :
    if s < 1 :
        return prefix_sum[e]
    value = prefix_sum[e] - prefix_sum[s-1]

    return value



for i in range(1,1000001) :
    prefix_sum[i] = prefix_sum[i-1] + arr[i]




for _ in range(q) :
    s,e = map(int, input().split())
    value = get_sum(s,e)
    print(value)