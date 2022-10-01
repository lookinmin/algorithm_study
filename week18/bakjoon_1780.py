# 분할정복, 실버2, 종이의 개수

from sys import stdin
n = int(stdin.readline())
paper = [list(map(int, input().split())) for _ in range(n)]

minus = 0
zero = 0
one = 0

def DAC(x, y, n):
    global minus, zero, one
    now = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if now != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        DAC(x + k * n//3, y + l * n//3, n//3)
                return

    if now == -1:
        minus += 1
    elif now == 0:
        zero += 1
    else:
        one += 1

DAC(0,0,n)
print(minus)
print(zero)
print(one)

