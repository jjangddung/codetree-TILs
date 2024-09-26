from sortedcontainers import SortedSet


n,m = map(int, input().split())

# s = SortedSet()


grid = list(map(int, input().split()))

# prev_length 랑 add한 length랑 비교 앉았는지 확인하기


ans_lst = []
maxi = 0

def backtraking(num) :
    global maxi
    if num == n :
        s = SortedSet()
        prev_length = 0
        for v in ans_lst :
            s.add(v)
            if prev_length == len(s) :
                maxi = max(len(s),maxi)
                return 
        
        maxi = max(len(s),maxi)

        return 


    
    for i in range(1,grid[num] +1 ) :
        ans_lst.append(i)
        backtraking(num+1)
        ans_lst.pop()


backtraking(0)
print(maxi)