#정렬, 브론즈2, 커트라인

from sys import stdin

n, k = map(int, stdin.readline().split())
x = list(map(int, stdin.readline().split()))
x.sort(reverse=True)

print(x[k-1])