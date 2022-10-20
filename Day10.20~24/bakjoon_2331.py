# 구현, 실버4, 반복수열

from sys import stdin

A, P = map(int, input().split())
arr = [A]


while True:
    res = 0
    for s in str(arr[-1]):
        res += int(s) ** P
    if res in arr:
        break

    arr.append(res)

print(arr.index(res))
