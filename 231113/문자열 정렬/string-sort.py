import sys

input = sys.stdin.readline

string = str(input().rstrip())

string = sorted(string)

string = ''.join(string)

print(string)