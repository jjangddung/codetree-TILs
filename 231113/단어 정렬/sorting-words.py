import sys

input =  sys.stdin.readline

N = int(input())

word_list = []

for i in range(N) :
    i = str(input().rstrip())
    word_list.append(i)

word_list.sort()

for word in word_list :
    print(word)