import sys

n,k,b = map(int, input().split())


# k개가 연속하기 위해선????
num_lst = []
for i in range(1,n+1) :
    num_lst.append(i)


zero_lst_index = []
for _ in range(b) :
    index = num_lst.index(int(input()))
    # print(index)
    num_lst[index] =  0
    zero_lst_index.append(index)
    # num_lst.pop(index)
    # print(num_lst)


# print(num_lst)
def backtracking(num,k) :
    if k == p :
        print(ans_lst)
        return 
    
    
    for i in range(num,n) :
        ans_lst.append(num)
        backtracking(num+1,k+1)
        ans_lst.pop()

result = sys.maxsize


for i in range(n-k+1) :
    count = 0
    for t in range(i,i+k) :
        if num_lst[t] == 0 :
            count +=1
    result = min(count, result)

print(result)