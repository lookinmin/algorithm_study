#구현, 브론즈3, 별찍기 13

from sys import stdin
n = int(stdin.readline())
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)