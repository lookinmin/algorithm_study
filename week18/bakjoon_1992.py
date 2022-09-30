# 분할정복, 실버1, 쿼드트리

from sys import stdin

n = int(stdin.readline())
quad = [list(map(int, input())) for _ in range(n)]


def DAC(x, y, n):
    now = quad[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if now != quad[i][j]:
                now = -1
                break

    if now == -1:
        print("(", end="")
        n = n//2
        DAC(x, y, n)
        DAC(x, y + n, n)
        DAC(x + n, y, n)
        DAC(x + n, y + n, n)
        print(")", end="")
    elif now == 1:
        print("1", end="")
    else:
        print("0", end="")


DAC(0, 0, n)
