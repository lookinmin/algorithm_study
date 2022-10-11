# 정렬, 실버4, 국영수

from sys import stdin
N = int(stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(stdin.readline().split()))

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in arr:
    print(i[0])


