import sys

input = sys.stdin.readline





class Sort()  :
    def __init__(self, arr) :
        self.arr = arr

        self.length = len(self.arr)


        self.origin = []
        self.T = []
        self.new = []

    
    def change(self) :
        for i in range(self.length) :
            k = [self.arr[i],i+1]
            self.T.append(k)
            self.origin.append(k)
        
        self.T.sort(key = lambda x : (x[0], x[1]))

        for i in range(self.length) :
            for j in range(self.length) :
                if self.origin[i] == self.T[j] :
                    self.new.append(j+1)
        
        
        

N = int(input())
num_input_list = list(map(int,input().split()))



sort = Sort(num_input_list)
sort.change()

for i in range(N) :
    print(sort.new[i], end= " ")