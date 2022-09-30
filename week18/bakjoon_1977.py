#구현, 브론즈2, 완전 제곱수

from sys import stdin
import math

m = int(stdin.readline())
n = int(stdin.readline())
arr = []
for i in range(m, n+1, 1):
    if math.sqrt(i) - int(math.sqrt(i)) == 0.0:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))


