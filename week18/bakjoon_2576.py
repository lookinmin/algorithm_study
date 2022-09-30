#구현, 브론즈3, 홀수

from sys import stdin
arr = []
for i in range(7):
    n = int(stdin.readline())
    if n % 2 == 1:
        arr.append(n)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))