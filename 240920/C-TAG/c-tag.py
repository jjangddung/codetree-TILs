import sys

n,m = map(int, input().split())


a_lst = []
b_lst = []

for i in range(n) :
    lst = str(input())
    a_lst.append(lst)
    

for i in range(n) :
    lst = str(input())
    b_lst.append(lst)


count = 0


def checking(s1,s2) :
    # if len(s1) != len(s2) :
        # return True
    for s in s1 :
        if s  in s2 :
            return False
    
    for s in s2 :
        if s  in s1 :
            return False
    
    return True

for i in range(m) :
    for j in range(i+1,m) :
        for k in range(j+1, m) :
            s1 = set()
            s2 = set()
            for t in range(n) :
                word1 = a_lst[t][i] + a_lst[t][j] + a_lst[t][k]
                word2 = b_lst[t][i] + b_lst[t][j] + b_lst[t][k]
                s1.add(word1)
                s2.add(word2)
            
            if checking(s1,s2) :
                count +=1
                # print(s1,s2)

print(count)