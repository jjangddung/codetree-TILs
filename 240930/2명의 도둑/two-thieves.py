import sys

# 가치는 = 무게*무게
# 사실상   주어진 것들 중에 두개 고르는 문제임 
# 범위는  r >>> 0 < < n
#         c >>>  0 << n-1
# 수로 표현을 하자 >>>>> n*n
# 최댓값은 어떻게 표현 ?? dp를 이용해서 접근하기
# dp[i][j] i번째를 포함했을 때 , j의 무게면서 최대 value


input = sys.stdin.readline
inf = -sys.maxsize

n,m,c = map(int, input().split())



grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# n = 3
# k = 2

def in_range(x,y) :
    return 0 <=x < n and 0 <= y < n


def overlap(one_r,third_r,one_e, second_s, second_e) :
    if one_r != third_r :
        return False

    if second_s <= one_e <= second_e :
        return True

    return False



def maxi(lst) :
    total = 0 
    if sum(lst) <= c :
        for v in lst :
            total += v**2
    
    return total

    length = len(lst)
    dp = [
        [inf] *(c+1)
        for _ in range(length+1) 
    ]

    dp[0][0] = 0
    result = -sys.maxsize

    for i in range(1,length+1) :
        for j in range(1,c+1) :

            if j - lst[i-1] < 0 :
                continue

            for t in range(i) :
                if dp[t][j-lst[i-1]] != inf :
                    dp[i][j] = max(dp[t][j-lst[i-1]] + lst[i-1]**2,dp[i][j])
            
            result = max(result, dp[i][j])
    # print(dp)
    # print(result)

    return result        


ans_lst = []

maximum = -sys.maxsize
def backtracking(num,k) :
    global maximum
    
    if num == n*n :
        if k == 2 :
            fisrt_v, second_v = ans_lst
            # print(fisrt_v,second_v)
            value = 0

            one_r, one_c = fisrt_v//n, fisrt_v%n # 첫번째 리스트 시작점
            second_c = one_c +m-1  # 첫번째 리스트 끝점
            third_r, third_c = second_v//n, second_v% n # 두 번째 리스트 시작점
            four_c =  third_c +m-1  # 두 번째 리스트 끝점

            if second_c >= n or four_c >= n :
                return 
            
            if overlap(one_r,third_r,second_c,third_c,four_c) :
                return 

            
            lst1 = grid[one_r][one_c:second_c+1]
            lst2 = grid[third_r][third_c:four_c +1]
            # print(lst1, lst2)

            result = maxi(lst1) + maxi(lst2)
# 
            # if fisrt_v == 0 and second_v == 13 :
                # print(lst1, lst2)
                # print(maxi(lst1), maxi(lst2))
            # print(result)
# 
            maximum = max(result, maximum)

                
            # print(ans_lst)
        return

    ans_lst.append(num)
    backtracking(num+1,k+1)
    ans_lst.pop()
    backtracking(num+1,k)

backtracking(0,0)

print(maximum)

# test = [5,7,5]
# result= maxi(test)
# print(result)