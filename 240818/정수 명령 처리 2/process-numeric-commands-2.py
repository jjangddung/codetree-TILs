from collections import deque



class  Queue :
    def __init__(self) :
        self.dq = deque()

    def push(self,item) :
        self.dq.append(item)
    
    def pop(self) :
        return (self.dq.popleft())
    
    def size(self) :
        return (len(self.dq))
    
    def empty(self) :
        if len(self.dq) == 0 :
            return 1
        else : 
            return 0
    
    def front(self) :
        return (self.dq[0])


n = int(input())

s= Queue()
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
        
        elif order == 'front' :
            print(s.front())
        
        else :
            print(s.empty())