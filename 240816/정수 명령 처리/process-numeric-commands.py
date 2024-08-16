class stack :
    def __init__(self) :
        self.items = []

    
    def push(self,item) :
        self.items.append(item)
    
    def empty(self) :
        if self.size() == 0 :
            return 1
        else :
            return 0


    
    def size(self) :
        return len(self.items)
    
    def pop(self) :
        if not self.empty() :
            return self.items.pop()
    
    def top(self) :
        if not self.empty() :
            return self.items[-1]


n = int(input())

s= stack()
for _ in range(n) :
    order = input()
    # print(order)

    try :
        n,m = order.split()
        # print(n,m)
        # print(m)
        m = int(m)
        s.push(m)
    
    except :
        if order == 'size' :
            print(s.size())
        elif order == 'pop' :
            print(s.pop())
        
        elif order == 'top' :
            print(s.top())
        
        else :
            print(s.empty())