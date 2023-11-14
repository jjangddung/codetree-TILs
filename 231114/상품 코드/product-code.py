import sys

input = sys.stdin.readline


class Product() :
    def __init__(self, name='codetree', code='50') :
        self.name = name
        self.code = code
    
    def printing(self) :
        print(f'product {self.code} is {self.name}')


def main() :
    question = tuple(map(str, input().split()))
    name =  question[0]
    code =  question[1]
    answer_1 = Product()
    answer_2 = Product(name, code)

    answer_1.printing()
    answer_2.printing()

if __name__ == '__main__' :
    main()