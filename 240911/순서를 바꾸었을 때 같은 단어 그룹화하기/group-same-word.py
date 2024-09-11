n = int(input())
d =  {}
maxi = 0
for _ in range(n) :
    sorted_word = sorted(str(input()))
    word = ""

    for i in range(len(sorted_word)) :
        word += sorted_word[i]
    
    if word not in d :
        d[word] = 1
    
    else :
        d[word] +=1
    
    maxi = max(maxi, d[word])

print(maxi)