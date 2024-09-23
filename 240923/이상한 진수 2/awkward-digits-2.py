word = str(input())

length = len(word)

n_lst = []

for i in range(length) :
    n_lst.append(int(word[i]))

count = 0

for v in range(1,length) :
    if n_lst[v] != 1 :
        n_lst[v] = 1
        count +=1
        break




result = 0

if count == 0 :
    n_lst[-1] = 0
    

n_lst = n_lst[::-1]
for i in range(length) :
    value = 2**i
    value = value *n_lst[i]
    result += value

print(result)