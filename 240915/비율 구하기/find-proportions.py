from sortedcontainers import SortedDict

sd = SortedDict()

n = int(input())

for i in range(n) :
    text = str(input())

    if text not in sd :
        sd[text] =1
    
    else :
        sd[text] +=1


for key, value in sd.items() :
    print(key, end= " ")
    result = 100*value/n
    formatted_num = "{:.4f}".format(result)
    print(formatted_num)