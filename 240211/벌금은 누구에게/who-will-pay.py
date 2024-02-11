import sys


input = sys.stdin.readline

n,m,k = map(int, input().split())



arr = [int(input()) for _ in range(m)]


n_list = [0 for _ in range(n+1)]






for i in arr :
    n_list[i] +=1

    if n_list[i] >= k :
        print(i)
        break

if max(n_list) < k :
    print(-1)