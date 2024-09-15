from sortedcontainers import SortedDict

sd = SortedDict()

n = int(input())


for i in range(n) :
    word = str(input())

    if word not in sd :
        sd[word] =1
    else :
        sd[word] +=1


for key , value in sd.items() :
    print(key, value)