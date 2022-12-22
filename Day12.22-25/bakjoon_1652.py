# 구현, 브론즈1, 누울 자리를 찾아라

import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]



row_can = 0
col_can = 0

for i in range(n):
    row_cnt = 0
    col_cnt = 0
    for j in range(n):
        if board[i][j] == ".":
            row_cnt += 1
        else:
            row_cnt = 0
        if row_cnt == 2:
           row_can += 1

        if board[j][i] == ".":
            col_cnt += 1
        else:
            col_cnt = 0
        if col_cnt == 2:
            col_can += 1

print(row_can, col_can)
