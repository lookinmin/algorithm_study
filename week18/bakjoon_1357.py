# 구현, 브론즈2, 뒤집힌 덧셈

from sys import stdin
x, y = stdin.readline().split()
revX = ''.join(reversed(x))
revY = ''.join(reversed(y))
res = str(int(revX) + int(revY))
print(int(''.join(reversed(res))))