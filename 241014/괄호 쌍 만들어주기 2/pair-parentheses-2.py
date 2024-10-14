import sys


string = str(input())

left_side =[]
right_side = []

count = 0
length = len(string)

for i in range(length-1) :
    if string[i] == '('  and string[i+1] == '(':
        left_side.append(i)
    
    elif string[i] == ')'  and string[i+1] == ')':
        right_side.append(i)


for l in left_side :
    for r in right_side :
        if r >l  :
            count +=1

print(count)