# 집합, 실버4, 듣보잡

from sys import stdin
n, m = map(int, stdin.readline().split())
arr1 = []
cnt = 0
res = set()
for i in range(n+m):
    arr1.append(input())

arr1.sort()
for i in range(1, len(arr1)):
    if arr1[i] == arr1[i-1]:
        cnt += 1
        res.add(arr1[i])

print(len(res))
for _ in res:
    print(_)