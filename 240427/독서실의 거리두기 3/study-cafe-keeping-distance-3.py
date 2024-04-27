import sys

input = sys.stdin.readline

n = int(input())

string = input()

x_list = []
dis_list = []

for i in range(n) :
    if string[i] == '1' :
        x_list.append(i)
maxi = 0

for i in range(1, len(x_list)) :
    dis = x_list[i] - x_list[i-1]
    dis_list.append(dis)
    maxi = max(dis_list)

dis_list.sort()
maxi_1 = maxi//2
maxi_2 = maxi - maxi_1
dis_list.append(maxi_1)
dis_list.append(maxi_2)
dis_list.sort()
print(min(dis_list))