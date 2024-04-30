n = int(input())
origin = 'A'
answer_list = []

for i in range(n) :
    answer_list.append(chr(ord('A')+ i))
    
alpha_list = list(map(str, input().split()))

index_list = []
for alpha in alpha_list :
    index =answer_list.index(alpha)
    index_list.append(index)

p  = n -1
count = 0
while p >= 0 :

    position =index_list.index(p)
    while position != p :
        index_list[position] , index_list[position+1] = index_list[position+1] , index_list[position]
        position =index_list.index(p)
        count +=1
    p -= 1

print(count)