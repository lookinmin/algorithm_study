# 구현, 브론즈1, 2차원 배열의 합
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, stdin.readline().split()))
    for j in range(1, m+1):
        arr[i][j] = temp[j-1]

k = int(stdin.readline())


for _ in range(k):
    i, j, x, y = map(int, stdin.readline().split())
    ans = 0
    for u in range(i, x + 1):
        for w in range(j, y + 1):
            ans += arr[u][w]
    print(ans)
