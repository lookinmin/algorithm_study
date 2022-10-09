# 정렬, 실버4, 로프

from sys import stdin

N = int(stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)
res = []
for i in range(1, N+1):
    res.append(i * arr[i-1])

print(max(res))