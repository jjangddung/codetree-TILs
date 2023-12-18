import sys

input =  sys.stdin.readline

sum  = 0

chance = 0
while True :
    N = int(input())
    chance += 1

    sum += N
    if  N < 20 or N > 29 :
        sum -= N
        chance -=1
        result = sum / chance
        print(format(result,".2f"))
        break