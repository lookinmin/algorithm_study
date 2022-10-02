#구현, 브론즈1, 단어 뒤집기

from sys import stdin
t = int(stdin.readline())

for i in range(t):
    str = list(input().split())
    for j in str:
        print(j[::-1], end=" ")


