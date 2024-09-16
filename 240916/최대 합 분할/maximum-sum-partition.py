import sys


n = int(input())

lst = list(map(int, input().split()))

lst= sorted(lst)

total_sum = sum(lst)


ans = []

value = 0


def making_dp(mid,length,new_lst) :
    dp = [
        [False]*(mid//2+1)
        
        for _ in range(length+1)
    ]

    for i in range(length) :
        dp[i][0] = True
    

    for i in range(1,length+1) :
        for j in range(1,mid//2+1) :
            if new_lst[i-1] <= j :
                dp[i][j] = dp[i-1][j] or dp[i-1][j-new_lst[i-1]]
            
            else :
                dp[i][j] = dp[i-1][j]
            
            if j == mid//2 :
                if dp[i][j] :
                    return True
    
    return False
    

def backtracking(num,t) :
    global value
    
    if num == n :
        if t == m :
            new_lst = []

            for v in range(n) :
                if v in ans :
                    continue
                new_lst.append(lst[v])
            
            mid = sum(new_lst)
            # print(new_lst)
            # print("mid: ", mid)

            if mid % 2  != 0 :
                return 

            if 2*value >= mid :
                return

            
            length = len(new_lst)
            if making_dp(mid, length,new_lst) :
                # print('here!')
                # print()
                value = max(value,mid//2)

        return 
    
    ans.append(num)
    backtracking(num+1,t+1)
    ans.pop()
    backtracking(num+1,t)


for i in range(0,n+1) :
    m = i
    backtracking(0,0)

print(value)