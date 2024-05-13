import sys

input = sys.stdin.readline


n,m, k = map(int, input().split())


num_list = list(map(int, input().split()))



answer = []


maxi_count = 0


def choose(num) :
    global maxi_count
    global k 
    if num == n +1  :
        matrix = [0]* (k+1)
        count  = 0
        for p in range(n) :
            j = answer[p]
            matrix[j] += num_list[p]
        
        for mat in matrix :
            if mat >= m-1 :
                count +=1
        
        maxi_count = max(count,maxi_count)

        return 

    
    for i in range(k) :
        answer.append(i)
        choose(num+1)
        answer.pop()

choose(1)
print(maxi_count)