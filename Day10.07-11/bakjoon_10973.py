# 구현, 실버3, 이전순열
E# 브루트 포스
from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

for i in range(N-1, 0, -1):
    if arr[i-1] > arr[i]:
        for j in range(N-1, 0, -1):
            if arr[i-1] > arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                print(*arr)
                exit()

print(-1)