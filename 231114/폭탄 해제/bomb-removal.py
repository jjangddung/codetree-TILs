import sys

class Bomb():
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def display_info(self):
        print(f'code : {self.code}')
        print(f'color : {self.color}')
        print(f'second : {self.second}')

def main():
    input_tuple = tuple(map(str, input().split()))

    code = input_tuple[0]
    color = input_tuple[1]
    second = input_tuple[2]

    bomb = Bomb(code, color, second)
    bomb.display_info()

if __name__ == '__main__':
    main()