# 기하학, 브론즈2, TV크기

from sys import stdin
D, H, W = map(int, stdin.readline().split())

r = D/((H**2 + W**2)**0.5)
print(int(H*r), int(W*r))