import sys

input = sys.stdin.readline


N = int(input())
num_list = []

num_1_list = list(map(int, input().split()))
num_2_list = list(map(int, input().split()))

num_1_list.sort()
num_2_list.sort()

if num_1_list == num_2_list :
    print('Yes')
else :
    print("No")