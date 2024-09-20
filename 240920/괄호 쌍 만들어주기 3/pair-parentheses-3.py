import sys

word = str(input())


length = len(word)

count = 0
for i in range(length) :
    for j in range(i+1, length) :
        if word[i]  + word[j] == '()' :
            count +=1


print(count)