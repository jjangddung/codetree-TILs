import sys

input = sys.stdin.readline


class Address() :
    def __init__(self,who) :
        self.name = who[0]
        self.number = who[1]
        self.place = who[2]     


    
    def displaying_info(self) :
        print(f'name {self.name}')
        print(f'addr {self.number}')
        print(f'city {self.place}')



def main() :
    N = int(input())
    p_list = []
    for j in range(N) :
        j = list(map(str, input().split()))
        p_list.append(j)
    p_list.sort()
    if len(p_list) == 1:
        people = p_list[0]
    else :
        people = p_list[-1]
    address = Address(people)
    address.displaying_info()
    


if __name__ == '__main__' :
    main()