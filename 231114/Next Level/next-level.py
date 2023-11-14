import sys

input = sys.stdin.readline

class Game :
    def __init__(self, ID = 'codetree', Level = 10) :
        self.name = ID
        self.lv = Level


game = Game()
a,b = map(str, input().split())
real = Game(a,b)

print(f'user {game.name} lv {game.lv}')
print(f'user {real.name} lv {real.lv}')