import sys

input = sys.stdin.readline


N = int(input())

_list = list(map(int, input().split()))
_list.sort()


result = _list[0]

# for i in _list :
    # mini =min(result, i)
    # maximum = max(result, i)
    # num_list = []
    # div =1
    # for k in range(1, mini//2 +1) :
        # if mini % k == 0 :
            # num_list.append(k)
            # num_list.append(mini//k)
    # num_list.sort()
    # for j in num_list :
        # if maximum % j == 0 :
            # div = j
    # result = result*i//div
# 
# 
# print(result)

def func(a,b) :
    mini = min(a,b)
    maximum = max(a,b)
    num_list = []
    div = 1
    for i in range(1,mini//2 +1) :
        if mini % i == 0 :
            num_list.append(mini//i)
            num_list.append(i)
    num_list.sort()
    for k in num_list :
        if maximum % k == 0 :
            div = k
    solve = a*b//div
    return solve

def LSM(t_list, N) :
    result = t_list[N-1]
    if N == 1 :
        result = t_list[N-1]
        return  result
    result = func(result, LSM(t_list,N-1))
    return result


print(LSM(_list,N))