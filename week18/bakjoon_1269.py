# 집합, 실버4, 대칭자집합

# A, B에 대해 A-B + B-A

from sys import stdin
n, m = map(int, stdin.readline().split())
a = set(map(int, stdin.readline().split()))
b = set(map(int, stdin.readline().split()))

c = set((a-b) | (b-a))
print(len(c))