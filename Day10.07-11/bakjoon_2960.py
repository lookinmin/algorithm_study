#구현, 실버4, 에라토스테네스의 체
# N보다 작거나 같은 모든 소수 찾기
import math
from sys import stdin
N, K = map(int, stdin.readline().split())

cnt = 0
arr = [True] * (N+1)

for i in range(2, len(arr) + 1):
    for j in range(i, N+1, i):
        if arr[j]:
            arr[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break
