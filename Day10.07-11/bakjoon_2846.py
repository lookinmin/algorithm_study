# 구현, 브론즈1, 오르막길

from sys import stdin

N = int(stdin.readline())
arr = list(map(int, input().split()))
res = []
tmp = 0
for i in range(1, len(arr)):

    if arr[i] > arr[i-1]:
        tmp += arr[i] - arr[i-1]
        if i == N-1:
            res.append(tmp)
    else:
        res.append(tmp)
        tmp = 0

print(max(res))
