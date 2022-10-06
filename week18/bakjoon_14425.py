# 집합, 실버3, 문자열 집합

from sys import stdin
n, m = map(int, stdin.readline().split())
s = set()
for i in range(n):
    s.add(stdin.readline())

check = []
for i in range(m):
    check.append(stdin.readline())

count = 0
for i in check:
    if i in s:
        count += 1

print(count)