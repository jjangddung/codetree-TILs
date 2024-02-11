import sys


input = sys.stdin.readline


n,t = map(int,input().split())




n_list = list(map(int, input().split()))


maximum = 0
s = 0
s_list = []

for i in range (n) :
    s = 0
    s_list = []

    for j in range(i,n) :
        if n_list[j] > t :
            s += 1
            # s_list.append(n_list[i])
            if j == n-1 :
                maximum = max(maximum,s)
                # print(s_list)
        else :
            
            maximum = max(maximum,s)
            # print(s_list)
            break

print(maximum)