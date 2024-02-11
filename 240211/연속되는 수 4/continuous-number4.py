import sys


input = sys.stdin.readline



n = int(input())


n_list = [int(input()) for _ in range(n)]


k = 0
maximum = 1



for i in range(n)  :
    s = 1
    k = n_list[i]

    for j in range(i+1,n) :
        if n_list[j] > k :
            k = n_list[j]
            s +=1
            if j == n-1 :
                maximum = max(s, maximum)

        
        else :
            maximum = max(s, maximum)
            break

print(maximum)