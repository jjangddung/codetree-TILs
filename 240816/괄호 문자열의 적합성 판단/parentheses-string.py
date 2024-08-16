class stack :
    def __init__(self) :
        self.items = []
    
    def push(self, item) :
        self.items.append(item)
    
    def pop(self) :
        self.items.pop()
    
    def empty(self) :
        if len(self.items)== 0 :
            return True
        
        else :
            return False

    def top(self) :
        if not empty():
            return self.items[-1]
    
    def size(self) :

        return len(self.items)



front = stack()
# back = stack() 

sign = str(input())
# print(len(sign))

count = 0
for i in range(len(sign)) :
    if i == 0 :
        if sign[i] == ')' :
            print('No')
            count +=1
            break
    
    if sign[i] == '(' :
        front.push('(')
    
    else :
        if not front.empty() :
            front.pop()
        
        else :
            # print(i)
            print('No')
            count +=1
            break

# print(*front.items)
if count == 0 :
    print('Yes')