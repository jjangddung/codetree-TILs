from collections import deque


class Deque :
    def __init__(self) :
        self.dq = deque()

    def push_front(self, item) :
        self.dq.appendleft(item)
    
    def push_back(self,item) :
        self.dq.append(item)
    
    def pop_front(self) :
        return (self.dq.popleft())
    
    def pop_back(self) :
        return self.dq.pop()


    def size(self) :
        return len(self.dq) 

    def empty(self) :
        if self.size() == 0 :
            return 1
        else :
            return 0
    
    def front(self) :
        return self.dq[0]
    
    def back(self) :
        return self.dq[-1]
    

n = int(input())
d = Deque()
for _ in range(n) :
    order = input()
    # print("order : ",order)
    try :
        main , num = map(str, order.split())
        # print("main: " ,main, "num: ", num)
        num = int(num)
        if main == 'push_back' :
            d.push_back(num)
        else :
            d.push_front(num)

    except :
        if order == 'front' :
            print(d.front())
        
        elif order == 'back' :
            print(d.back())
        
        elif order == 'size' :
            print(d.size())
        
        elif order == 'empty' :
            print(d.empty())
        elif order == 'pop_front' :
            print(d.pop_front())

        elif order == 'pop_back' :
            print(d.pop_back())