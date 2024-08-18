from collections import deque


class Queue() :
    def __init__(self) :
        self.dq = deque()
    
    def push(self, item) :
        self.dq.append(item)
    
    def pop(self) :
        return self.dq.popleft()

    def size(self) :
        return len(self.dq)
    

n,m = map(int , input().split())

q = Queue()
count = 1
for i in range(1,n+1) :
    q.push(i)

while q.size() != 0 :
    if count < m :
        q.push(q.pop())
        count +=1
    else :
        print(q.pop(), end= " ")
        count =1