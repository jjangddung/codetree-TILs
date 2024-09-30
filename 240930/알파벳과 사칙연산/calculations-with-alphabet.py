import sys

input= sys.stdin.readline

# 그냥 값을 미리 지정하기 
given = str(input())
word_lst =[]
math_lst = []


for s in range(len(given)) :
    if given[s] == '-' or given[s] == '+' or given[s] == '*'  :
        math_lst.append(given[s])
    
    else :
        word_lst.append(given[s])


# print(word_lst, math_lst)

word_set = set(word_lst)

word_set = list(word_set)

ans_lst = []
maxi = -sys.maxsize
prev_lst = []

def backtracking(num,k) :
    global maxi
    if k == 6 :
        # print(ans_lst)
        real_lst = []
        result_lst = []


        for v in word_lst :
            if v == 'a' :
                real_lst.append(str(ans_lst[0]))
            
            elif v == 'b' :
                real_lst.append(str(ans_lst[1]))
            
            elif v == 'c' :
                real_lst.append(str(ans_lst[2]))
            
            elif v == 'd' :
                real_lst.append(str(ans_lst[3]))
            
            elif v == 'e' :
                real_lst.append(str(ans_lst[4]))
            
            else :
                real_lst.append(str(ans_lst[5]))
        
        result_lst.append(real_lst[0])

        for i in range(1, len(word_lst)) :
            result_lst.append(math_lst[i-1])
            result_lst.append(real_lst[i])
        
        value = 0
        for i in range(0,len(result_lst),2) :
            if i  == 0 :
                value += int(result_lst[i])
                continue
            
            if result_lst[i-1] == '-' :
                value -= int(result_lst[i])
            
            elif result_lst[i-1] == '+' :
                value += int(result_lst[i])
            
            elif result_lst[i-1] == '*' :
                value *= int(result_lst[i])

        
        maxi = max(value, maxi)

        return 

    
    for elem in range(1,5) :
        ans_lst.append(elem)
        backtracking(elem,k+1)
        ans_lst.pop()

backtracking(1,0)
print(maxi)