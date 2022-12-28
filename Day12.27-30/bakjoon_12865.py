# DP, 골드5, Knapsack Problem
# 평범한 배낭 : 0-1 Knapsack

from sys import stdin

n, k = map(int, stdin.readline().split())
item = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    item.append(list(map(int, stdin.readline().split())))

for i in range(1, n+1):         # i = 현재 담을 물건의 인덱스
    for j in range(1, k+1):     # j = 현재 가방의 허용 용량
        w = item[i][0]          # 현재 담을 물건의 무게
        v = item[i][1]          # 현재 담을 물건의 가치

        if j < w:               # 현재 배낭 허용 무게보다 물건이 무겁다면 넣지 않는다.
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)

print(d[n][k])

