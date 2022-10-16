# 문자열, 실버4, 베스트셀러

from sys import stdin
N = int(input())
arr = []
res = {}
for i in range(N):
    arr.append(input())

for i in arr:
    res[i] = arr.count(i)

k = max(res.values())
ans = []
for i, j in res.items():
    if j == k:
        ans.append(i)

print(sorted(ans)[0])
