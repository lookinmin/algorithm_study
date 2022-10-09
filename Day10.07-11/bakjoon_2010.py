# 구현, 브론즈3, 플러그

from sys import stdin

N = int(stdin.readline())
arr = []
for i in range(N):
    arr.append(int(stdin.readline()))

res = sum(arr) - (N-1)
print(res)