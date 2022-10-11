# 구현, 브론즈2, 농구 경기

from sys import stdin

N = int(stdin.readline())
arr = []
for _ in range(N):
    a = stdin.readline()
    arr.append(a[0])

name = set(arr)
res = []
for i in name:
    if arr.count(i) >= 5:
        res.append(i)

if len(res) > 0:
    print("".join(sorted(res)))
else:
    print("PREDAJA")