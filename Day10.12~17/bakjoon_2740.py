# 구현, 실버5, 행렬곱
from sys import stdin
N, M = map(int, stdin.readline().split())
arr1 = []
arr2 = []
for _ in range(N):
    arr1.append(list(map(int, stdin.readline().split())))
M, K = map(int, stdin.readline().split())
for _ in range(M):
    arr2.append(list(map(int, stdin.readline().split())))

res = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for m in range(M):
            res[i][j] += arr1[i][m] * arr2[m][j]

for i in res:
    for j in i:
        print(j, end= " ")
    print()