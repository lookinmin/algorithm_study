# 구현, 브론즈1, 색종이

# 가로 세로 10
# a = y축부터 거리, b = x축부터 거리
from sys import stdin
N = int(stdin.readline())
board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

answer = 0
for row in board:
    answer += row.count(1)
print(answer)

