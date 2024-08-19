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

grid = deque([i for i in range(1,n+1)])

while len(grid) != 1 :
    grid.popleft()
    grid.append(grid.popleft())

print(grid[0])